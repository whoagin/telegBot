import telebot
import requests
from config import TOKEN, keys


class BaseTgBotException(Exception):

    def __init__(self, message, *args):
        message = f'произошла ошибка: {message}'
        super().__init__(message, *args)


class APIException(BaseTgBotException):
    pass


class ConvertionException(BaseTgBotException):
    pass


bot = telebot.TeleBot(TOKEN)


class CryptoConvertor:
    @staticmethod
    def get_price(quote: str, base: str):

        if quote.lower() == base.lower():
            raise ConvertionException(f'Введены одинаковые валюты {quote}')

        if quote.lower() and base.lower() not in keys:
            raise APIException(f'Валюты введены не верно!\nпосмотреть список валют /values')

        url = f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote.lower()]}&tsyms={keys[base.lower()]}'



        return url

    def get_data_by_url(url: str) -> dict:
        result = requests.get(url)
        if result.status_code == 200:
            return result.json()
        raise APIException(f'Ошибка выполнения запроса, с статус кодом {result.status_code}')
