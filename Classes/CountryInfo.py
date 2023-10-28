import requests
from bs4 import BeautifulSoup


class CountryInfo:
    def __init__(self, country):
        self.country = country

    def get_info(self):
        country = self.country
        url = f'https://tradingeconomics.com/{country}/indicators'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        tr_lst = soup.find('tbody').text.split()

        gdp_info_start_index = 27
        gdp_info_finish_index = 33
        unemployment_info_start_index = 35
        unemployment_info_finish_index = 41
        inflation_info_start_index = 43
        inflation_finish_start_index = 49
        interest_info_start_index = 60
        interest_info_finish_index = 66

        if country == 'russia':
            damper = -9
            gdp_info = tr_lst[gdp_info_start_index + damper:gdp_info_finish_index + damper][0]
            unemployment_info = tr_lst[unemployment_info_start_index +
                                       damper:unemployment_info_finish_index + damper][0]
            inflation_info = tr_lst[inflation_info_start_index + damper:inflation_finish_start_index + damper][0]
            interest_info = tr_lst[interest_info_start_index + damper:interest_info_finish_index + damper][0]
        elif country == 'united-states':
            damper = 9
            gdp_info = tr_lst[gdp_info_start_index:gdp_info_finish_index][0]
            unemployment_info = tr_lst[unemployment_info_start_index:unemployment_info_finish_index][0]
            inflation_info = tr_lst[inflation_info_start_index + damper:inflation_finish_start_index + damper][0]
            interest_info = tr_lst[interest_info_start_index + damper:interest_info_finish_index + damper][0]
        elif country == 'japan' or country == 'canada':
            damper = 9
            gdp_info = tr_lst[gdp_info_start_index:gdp_info_finish_index][0]
            unemployment_info = tr_lst[unemployment_info_start_index +
                                       damper:unemployment_info_finish_index + damper][0]
            inflation_info = tr_lst[inflation_info_start_index + damper:inflation_finish_start_index + damper][0]
            interest_info = tr_lst[interest_info_start_index + damper:interest_info_finish_index + damper][0]
        elif country == 'india':
            damper = -9
            gdp_info = tr_lst[gdp_info_start_index:gdp_info_finish_index][0]
            unemployment_info = tr_lst[unemployment_info_start_index:unemployment_info_finish_index][0]
            inflation_info = tr_lst[inflation_info_start_index:inflation_finish_start_index][0]
            interest_info = tr_lst[interest_info_start_index + damper:interest_info_finish_index + damper][0]
        elif country == 'brazil':
            damper = -1
            gdp_info = tr_lst[gdp_info_start_index + damper:gdp_info_finish_index + damper][0]
            unemployment_info = tr_lst[unemployment_info_start_index +
                                       damper:unemployment_info_finish_index + damper][0]
            inflation_info = tr_lst[inflation_info_start_index + damper:inflation_finish_start_index + damper][0]
            interest_info = tr_lst[interest_info_start_index + damper:interest_info_finish_index + damper][0]
        else:
            gdp_info = tr_lst[gdp_info_start_index:gdp_info_finish_index][0]
            unemployment_info = tr_lst[unemployment_info_start_index:unemployment_info_finish_index][0]
            inflation_info = tr_lst[inflation_info_start_index:inflation_finish_start_index][0]
            interest_info = tr_lst[interest_info_start_index:interest_info_finish_index][0]
        return gdp_info, unemployment_info, inflation_info, interest_info


