import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


owm = OWM('Your openweathermap key')
mgr = owm.weather_manager()
bot = telebot.TeleBot("Your bot key")

config_dict = get_default_config()
config_dict['language'] = 'ru' 

@bot.message_handler(content_types=["text"])
def send_echo(message):
	
	observation = mgr.weather_at_place (message.text)
	w = observation.weather

	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "." "\n"
	answer += "Температура в районе: " + str(temp) + " градусов" + "." "\n\n"

	if temp < 10:
		answer += "Очень холодно, одевайся теплее!"
	elif temp < 18:
		answer += "Не так уж и холодно, но легкая куртка не помешает."
	elif temp < 25:
		answer += "Сегодня жарко, можно надеть шорты."
	elif temp > 25:
		answer += "Осторожнее на солнце, сегодня настоящее пекло."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )