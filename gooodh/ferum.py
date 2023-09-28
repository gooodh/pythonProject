
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')



cookies = {
    'csrftoken': 'R0QyHEolNvpXWDmbxSfltl4x5ur2BkXb',
    'sessionid': 'kz6n00ejffd4gnrgwfqunbffoivns06a',
}

headers = {
    'authority': 'ferum-dsg.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'csrftoken=R0QyHEolNvpXWDmbxSfltl4x5ur2BkXb; sessionid=kz6n00ejffd4gnrgwfqunbffoivns06a',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}




def get_source_html():
    response = requests.get('https://ferum-dsg.ru/', cookies=cookies, headers=headers)
    with open('ferum.html', 'w', encoding='utf-8') as file:
        file.write(response.text)


def get_result():
    with open('index.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    item_phones = soup.find("div", class_="container")#.find("div", class_="content").find("div", class_="uni-wrapper").find('products-block row row-flex').find_all("div", class_="product-layout product-grid grid-view col-sm-6 col-md-4 col-lg-4 col-xxl-5")
    print(item_phones)

    
if __name__ == '__main__':
   
    get_source_html()
    # get_result()
