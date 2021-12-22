import os
import telebot
from telebot import types
import cfg_file

# Токен бота
TOKEN = cfg_file.Token

# Сообщения
mes_multi1 = 'Вывести мультиметр1'
mes_multi2 = 'Вывести мультиметр2'
mes_multi3 = 'Вывести мультиметр3'
mes_all = 'Вывести все'
mes_count = 'Вывести количество мультиметров'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['info'])
def give_info(message):
    bot.reply_to(message, 'Я демонстрирую фото мультиметров, находящиеся в наличии,'
                          ' а также сообщаю их количество. Нажмите кнопку.')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Идентификатор диалога
    chat_id = message.chat.id

    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text

    # Проверка сообщения и вывод данных
    if text == mes_multi1:
        img = open(os.path.join(cur_path, 'pictures\Мультиметр1.png'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == mes_multi2:
        img = open(os.path.join(cur_path, 'pictures\Мультиметр2.png'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == mes_multi3:
        img = open(os.path.join(cur_path, 'pictures\Мультиметр3.png'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == mes_all:
        for i in range(3):
            img = open(os.path.join(cur_path, f'pictures\Мультиметр{i+1}.png'), 'rb')
            bot.send_photo(chat_id, img)
    elif text == mes_count:
        bot.send_message(chat_id, 'Доступно мультиметров: 3')
    else:
        markup = types.ReplyKeyboardMarkup(row_width=5)
        itembtn1 = types.KeyboardButton(mes_multi1)
        itembtn2 = types.KeyboardButton(mes_multi2)
        itembtn3 = types.KeyboardButton(mes_multi3)
        itembtn4 = types.KeyboardButton(mes_all)
        itembtn5 = types.KeyboardButton(mes_count)
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)


bot.infinity_polling()
