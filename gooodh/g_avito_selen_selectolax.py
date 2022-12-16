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

from sec_time import sec_timer

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
        time.sleep(120)
        # button = driver.find_element(By.CLASS_NAME, 'desktop-1kdcmzd')
        # time.sleep(10)
        # button.click()

        # action = ActionChains(driver)
        # action.move_to_element("iframe").perform()
        # time.sleep(3)

        # # Get scroll height
        # last_height = driver.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(1)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #
        #     if new_height == last_height:# до конца страницы мотает
        #         break
        #     last_height = new_height

        # поиcк json
        tree = HTMLParser(driver.page_source)
        scripts = tree.css('script')

        for script in scripts:
            if 'window.__initialData__' in script.text():
                json_text = script.text().split(';')[0].split('=')[-1].strip()
                json_text = unquote(json_text)
                json_text = json_text[1:-1]
                json_data = json.loads(json_text)
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, ensure_ascii=False)
                # with open('page.html', 'w', encoding='utf-8') as file:
                #     file.write(driver.page_source)
                print('file save')

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def get_result():
    # offers = {}
    with open('data.json', 'r', encoding='utf-8') as file:
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
    for key in json_data:
        if 'single-page' in key:
            for item in json_data[key]['data']['recommendationsInfinite']['items']:
                timestamp = datetime.fromtimestamp(item['sortTimeStamp'])
                timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
                url_off = 'https://www.avito.ru' + item['urlPath']

                with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
                    writer = csv.writer(file)

                    writer.writerow(
                        [
                            item['id'],
                            item['title'],
                            item['location']['name'],
                            item['priceDetailed']['value'],
                            item['priceDetailed']['postfix'],
                            timestamp,
                            url_off.strip()
                        ]
                    )

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

    for key in json_data:
        if 'single-page' in key:
            for items in json_data[key]['data']['vertical-widgets']:
                if type(items['value'].get('items')) != type(None):
                    for item in items['value'].get('items'):
                        if type(item.get('value')) != type(None):
                            timestamp = datetime.fromtimestamp(item.get('value')['sortTimeStamp'] / 1000)
                            timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
                            url_off = 'https://www.avito.ru' + item.get('value')['urlPath']
                            geo_a = item.get('value')['geo']['geoReferences'][0]['content'] + ' ' + \
                                    item.get('value')['geo']['formattedAddress']

                            with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(
                                    [
                                        item.get('value')['id'],
                                        item.get('value')['title'],
                                        geo_a,
                                        item.get('value')['priceDetailed']['value'],
                                        item.get('value')['priceDetailed']['postfix'],
                                        timestamp,
                                        url_off.strip()
                                    ]
                                )


if __name__ == '__main__':
    url = 'https://www.avito.ru/barnaul/nedvizhimost?cd=1'
    get_source_html(url)
    get_result()
