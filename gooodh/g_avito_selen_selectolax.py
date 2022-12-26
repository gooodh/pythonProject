from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selectolax.parser import HTMLParser
from urllib.parse import unquote

import time
from datetime import datetime
import json
import csv

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')


def get_source_html(url):
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(ua.random)
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(10)
        json_data = driver.page_source
        json_data = json_data.split('>')[6].split('<')[0]
        json_data = json.loads(json_data)
        get_result(json_data)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def get_result(json_data):
    # with open('data.json', 'r', encoding='utf-8') as file:
    #     json_data = json.load(file)

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
    # for key in json_data:

    # if 'single-page' in key:
    #     for item in json_data[key]['data']['recommendationsInfinite']['items']:
    #         timestamp = datetime.fromtimestamp(item['sortTimeStamp'])
    #         timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
    #         url_off = 'https://www.avito.ru' + item['urlPath']
    #
    #         with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
    #             writer = csv.writer(file)

    # writer.writerow(
    #     [
    #         item['id'],
    #         item['title'],
    #         item['location']['name'],
    #         item['priceDetailed']['value'],
    #         item['priceDetailed']['postfix'],
    #         timestamp,
    #         url_off.strip()
    #     ]
    # )

    # offer = {}
    # # offer['id'] = item['id']
    # offer['title'] = item['title']
    # timestamp = datetime.fromtimestamp(item['sortTimeStamp'])
    # timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
    # offer['price'] = item['priceDetailed']['value']
    # offer['postfix'] = item['priceDetailed']['postfix']
    # offer['location'] = item['location']['name']
    # offer['url'] = 'https://www.avito.ru' + item['urlPath']
    # offers[item['id']] = offer


if __name__ == '__main__':
    # url = 'https://www.avito.ru/web/1/main/items?forceLocation=false&locationId=621630&lastStamp=1672027185&limit=30&offset=54&categoryId=4'
    url = 'https://www.avito.ru/web/1/main/items?forceLocation=false&locationId=621630&lastStamp=1672041950&limit=30&offset=29&categoryId=5'

    get_source_html(url)
