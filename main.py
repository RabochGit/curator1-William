import telebot


bot = telebot.TeleBot('6521754221:AAG710QBWexJsmYb14BJk0JVH0H1M8J_ZqM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет. Это бот, который поможет тебе в партии в ДнД и за тебя очень хорошо '
                                      'бросит дайсы. Всё, что тее нужно -- ткнуть нужную команду!\n\n Всё просто! '
                                      'Есть следующие кубы: \n\n/d100 - Для броска стогранника \n/d20 - Для броска '
                                      'классического двадцатигранника \n/d12 -- для броска 12гранника\n/d10 - '
                                      'десятигранник\n/d8 - восьмигранник\n/d6 -- обычный шестигранник\n/d4 - '
                                      'четырёхгранник', parse_mode='Markdown')

@bot.message_handler(commands=['d100'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 100. \nПоздравляю! ещё раз? /d100 ', parse_mode='Markdown')

@bot.message_handler(commands=['d20'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 20. \nПоздравляю! ещё раз? /d20', parse_mode='Markdown')

@bot.message_handler(commands=['d12'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 12. \nПоздравляю! ещё раз? /d12 ', parse_mode='Markdown')

@bot.message_handler(commands=['d10'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 10. \nПоздравляю! ещё раз? /d10 ', parse_mode='Markdown')

@bot.message_handler(commands=['d8'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 8. \nПоздравляю! ещё раз? /d8 ', parse_mode='Markdown')


@bot.message_handler(commands=['d6'])
def main(message):
    bot.send_message(message.chat.id, 'Результат броска - 6. \nПоздравляю! ещё раз? /d6 ', parse_mode='Markdown')


@bot.message_handler(commands=['d4'])
def main(message):
    bot.send_message(message.chat.id, "Результат броска - 4. \nПоздравляю! ещё раз? /d4 ", parse_mode='Markdown')


bot.infinity_polling()
