
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')


cookies = {
    'ks.ngs.s': '1ba0258786c7a7bcfa4b8cf286f04533',
    'k_stat': '1b75171a-c152-430d-818e-f5c0abd0d3be',
    'ks.tg': '100',
    'ssaid': '546e48c0-b28d-11ed-b2bf-33e5cb8e8e44',
    '_hjSessionUser_283363': 'eyJpZCI6ImU4MjZjMzg5LTYwNTAtNTc2NC1hYjQzLWYzMDBkMDE3MDc0OSIsImNyZWF0ZWQiOjE2NzcwNTU1NjA0MDQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample': '1',
    '_hjSession_283363': 'eyJpZCI6ImUzYjAwMDA4LWI4ZDEtNDA1YS05NmU3LTVjOGE4ZTFmMDkxMSIsImNyZWF0ZWQiOjE2NzcwNTU1NjA2MjUsImluU2FtcGxlIjp0cnVlfQ==',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '1',
    '_ym_uid': '1677055561135114265',
    '_ym_d': '1677055561',
    '_ga': 'GA1.2.714309875.1677055561',
    '_gid': 'GA1.2.2006778753.1677055561',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'kaspi.storefront.cookie.city': '750000000',
    'ks.cc': '-1',
    '_gat_ddl': '1',
    '__tld__': 'null',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Language': 'ru-RU',
    'Connection': 'keep-alive',
    'Referer': 'https://kaspi.kz/shop/c/kitchen%20chairs/',
    # 'Cookie': 'ks.ngs.s=1ba0258786c7a7bcfa4b8cf286f04533; k_stat=1b75171a-c152-430d-818e-f5c0abd0d3be; ks.tg=100; ssaid=546e48c0-b28d-11ed-b2bf-33e5cb8e8e44; _hjSessionUser_283363=eyJpZCI6ImU4MjZjMzg5LTYwNTAtNTc2NC1hYjQzLWYzMDBkMDE3MDc0OSIsImNyZWF0ZWQiOjE2NzcwNTU1NjA0MDQsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_283363=eyJpZCI6ImUzYjAwMDA4LWI4ZDEtNDA1YS05NmU3LTVjOGE4ZTFmMDkxMSIsImNyZWF0ZWQiOjE2NzcwNTU1NjA2MjUsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _ym_uid=1677055561135114265; _ym_d=1677055561; _ga=GA1.2.714309875.1677055561; _gid=GA1.2.2006778753.1677055561; _ym_visorc=b; _ym_isad=2; kaspi.storefront.cookie.city=750000000; ks.cc=-1; _gat_ddl=1; __tld__=null',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}




def get_source_json():
    response = requests.get(
    'https://kaspi.kz/yml/product-view/pl/results?q=%3Acategory%3AKitchen%20chairs%3AavailableInZones%3AMagnum_ZONE1&text&page=1&sort=relevance&qs&ui=d&i=-1',
    cookies=cookies,
    headers=headers,
)
    with open(f'avito.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False)

def get_result():

    with open('avito.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)


    with open(f'avito{cur_time}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                'id',
                'Название',
                'Локация',
                'Цена',
                'Примечание',
                'Дата, время публикации',
                'Url'
            ]
        )

   
        
    for item in json_data['items']:

        category = item['category']['slug']
        if category in 'kvartiry':
            
            title = item['title'].replace('&nbsp;', ' ')
            timestamp = datetime.fromtimestamp(item['sortTimeStamp'])
            timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
            url_off = 'https://www.avito.ru' + item['urlPath'].strip()

            with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
                writer = csv.writer(file)

                writer.writerow(
                    [
                        item['id'],
                        title,
                        item['location']['name'],
                        item['priceDetailed']['value'],
                        item['priceDetailed']['postfix'],
                        timestamp,
                        url_off
                    ]
                )

if __name__ == '__main__':
   
    get_source_json()
    # get_result()

