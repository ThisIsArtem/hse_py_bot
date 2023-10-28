import requests
from dateutil.parser import parse


class CurrencyConvertor:
    """Класс для информации об официальном курсе валют с сайта ЦБ РФ
    Атрибуты класса:
    currency_from - код валюты из которой происходит конвертация, в соответствии с международным правилом
    currency_from - код валюты в которую происходит конвертация, в соответствии с международным правилом
    (например, USD, EUR, CNY)
    """
    def __init__(self, cf, ct, am):
        self.currency_from = cf
        self.currency_to = ct
        self.amount = am

    def convertor(self):
        """ Для конвертации используется open.er-api
        :return: кортеж вида (дата и время обновления курса, итог конвертации)
        """
        src = self.currency_from
        dst = self.currency_to
        amount = self.amount
        url = f"https://open.er-api.com/v6/latest/{src}"
        data = requests.get(url).json()
        if data["result"] == "success":
            last_updated_datetime = parse(data["time_last_update_utc"])
            exchange_rates = data["rates"]
            return last_updated_datetime, exchange_rates[dst] * amount

