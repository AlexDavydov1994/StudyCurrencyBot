import telebot
from config import TOKEN
from extensions import ConvertionException,CurrencyConverter,currency


bot = telebot.TeleBot(TOKEN)





@bot.message_handler(commands=['start', 'help'])
def send_welcome(message:telebot.types.Message):
    text='Чтобы начать работу с ботом:\nВведите:\n <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n Увидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def conver_currency(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base=CurrencyConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.{e}')
    except Exception as e:
        bot.reply_to(message,f' Не удалось обработать команду\n{e}')
    else:
        text=f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id,text)
bot.polling(none_stop=True)#запуск бота
