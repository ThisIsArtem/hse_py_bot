import requests
from bs4 import BeautifulSoup


class ExchangeRate:
    def __init__(self, code):
        self.code = code

    def get_info(self):
        url = f'https://cbr.ru/currency_base/daily/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        tr_lst = soup.find_all('td')
        for i in range(len(tr_lst)):
            tr_lst[i] = tr_lst[i].text
        print(tr_lst)
        exchangerate_index = tr_lst.index(self.code)
        value = float(tr_lst[exchangerate_index + 3].replace(',', '.'))
        nums = int(tr_lst[exchangerate_index + 1])
        exchangerate = value / nums
        return exchangerate


result = ExchangeRate('AMD').get_info()
print(result)
