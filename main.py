import telebot

bot = telebot.TeleBot('6493874150:AAHCYEpM0ibzow7T5YEAmu-9JtvbNR_ss-k')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'hola', parse_mode='Markdown')


@bot.message_handler(commands=['vær'])
def main(message):
    bot.send_message(message.chat.id, 'Flott vær i dag', parse_mode='Markdown')


@bot.message_handler(commands=['hvordan går det'])
def main(message):
    bot.send_message(message.chat.id, 'det går bra', parse_mode='Markdown')


bot.infinity_polling()