import telebot
from time import sleep


with open("secrets/token") as file:
    token = file.read()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    mess1 = 'Запускаю тест на пидора, подождите'
    bot.send_message(message.chat.id, mess1, parse_mode = 'html')
    sleep(3)
    mess2 = f'Твое имя - {message.from_user.first_name}, значит <b>ты пидор</b>'
    bot.send_message(message.chat.id, mess2, parse_mode = 'html')

if __name__ == '__main__':
     bot.infinity_polling(none_stop = True)