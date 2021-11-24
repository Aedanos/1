import pyowm
import telebot
owm = pyowm.OWM('d66ee64fca95004c449a8b632b9c3367')
bot = telebot.TeleBot("2133620366:AAEvwjkQqLG5yxGIwVdpOqe5OsaG01LBD4o")
mgr = owm.weather_manager()


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place('Khmelnytskyi')
	w = observation.weather
	temp = w.temperature('celsius')["temp"]
	rain = w.rain
	clouds = w.clouds

	answer =  w.detailed_status + str(temp) + str(rain) + str(clouds)

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )