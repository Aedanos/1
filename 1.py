import telebot

bot = telebot.TeleBot("2133620366:AAEvwjkQqLG5yxGIwVdpOqe5OsaG01LBD4o")

@bot.message_handler(contact_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop = True)
