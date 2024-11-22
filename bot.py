from utill import *


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \nУвдеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:

        if not len(message.text.split()) == 3:
            bot.reply_to(message, 'Неверно введены данные!\n Пример [доллар биткойн 5]')
            raise ConvertionException('Некорректное кол-во параметров')

        quote, base, amount = message.text.split(" ")

        response_result = CryptoConvertor.get_data_by_url(CryptoConvertor.get_price(quote, base))
        end_word = base[0:-1] + 'ях' if base[-1] == 'ь' else base + 'ах'
        response_text = f'Цена {amount} {quote.lower()}ов в {end_word.lower()} = {response_result[keys[base.lower()]] * float(amount)} '
        bot.send_message(message.chat.id, response_text)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling()
