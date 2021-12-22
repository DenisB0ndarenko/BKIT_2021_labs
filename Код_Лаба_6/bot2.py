import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Я умею проверять представителей знаков Зодиака на совместимость!\n'
                                      '0 - Овен\n'
                                      '1 - Телец\n'
                                      '2 - Близнецы\n'
                                      '3 - Рак')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    bot.send_message(message.chat.id, 'Введите номер первого знака Зодиака')


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущих вводов.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    bot.send_message(message.chat.id, 'Введите номер первого знака Зодиака')


# Обработка первого числа (знака Зодиака)
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_FIRST_NUM.value)
def first_num(message):
    text = message.text
    if not (text.isdigit() and int(text)>=0 and int(text)<=config.Zodiac.__len__()-1):
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите подходящий номер!')
        return
    else:
        bot.send_message(message.chat.id, f'Ваш первый знак Зодиака - {config.Zodiac[int(text)]}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
        # Сохраняем первое число (знак Зодиака)
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value), text)
        bot.send_message(message.chat.id, 'Введите номер второго знака Зодиака')


# Обработка второго числа (знака Зодиака)
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SECOND_NUM.value)
def second_num(message):
    text = message.text
    if not (text.isdigit() and int(text)>=0 and int(text)<=config.Zodiac.__len__()-1):
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите подходящий номер!')
        return
    else:
        bot.send_message(message.chat.id, f'Ваш второй знак Зодиака - {config.Zodiac[int(text)]}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
        # Сохраняем второе число (знак Зодиака)
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value), text)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Любовь')
        itembtn2 = types.KeyboardButton('Работа')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, 'Выберите пожалуйста тип отношений', reply_markup=markup)


# Выбор типа отношений
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
def relation(message):
    # Текущий тип отношения
    rltn = message.text
    # Читаем номера знаков Зодиака из базы данных
    s1 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value))
    s2 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value))
    # Выводим результат
    markup = types.ReplyKeyboardRemove(selective=False)

    if config.conclusion(s1, s2, rltn):
        bot.send_message(message.chat.id, f'Результат: {config.Zodiac[int(s1)]} и {config.Zodiac[int(s2)]} {"cовместимы"}'
                                          f' при типе отношений: {rltn}', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Результат: {config.Zodiac[int(s1)]} и {config.Zodiac[int(s2)]} {"неcовместимы"}'
                                          f' при типе отношений: {rltn}', reply_markup=markup)
    # Меняем текущее состояние
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    # Выводим сообщение
    bot.send_message(message.chat.id, 'Введите номер первого знака Зодиака')


if __name__ == '__main__':
    bot.infinity_polling()
