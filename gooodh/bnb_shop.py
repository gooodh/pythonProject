
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')

cookies = {
    'OCSESSID': '786374665eda26c58d20c8408c',
    'language': 'ru-ru',
    'currency': 'RUB',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://bnb-shop.ru/index.php?route=product/category&path=86_87_66',
    'Connection': 'keep-alive',
    # 'Cookie': 'OCSESSID=786374665eda26c58d20c8408c; language=ru-ru; currency=RUB',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
def get_source_html():
     
    response = requests.get(
        'https://bnb-shop.ru/index.php?route=product/category&path=86_87_66_71',
        cookies=cookies,
        headers=headers,
        )

    with open('bnb.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
def get_result():
    with open('index.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    item_phones = soup.find("div", class_="container")#.find("div", class_="content").find("div", class_="uni-wrapper").find('products-block row row-flex').find_all("div", class_="product-layout product-grid grid-view col-sm-6 col-md-4 col-lg-4 col-xxl-5")
    print(item_phones)
if __name__ == '__main__':
   
    # get_source_html()
    get_result()