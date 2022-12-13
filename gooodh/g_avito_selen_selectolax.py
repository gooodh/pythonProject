from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selectolax.parser import HTMLParser
from urllib.parse import unquote

import time
import json
from selenium.webdriver.common.by import By


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
        # button = driver.find_element(By.CLASS_NAME, 'desktop-1kdcmzd')
        # time.sleep(10)
        # button.click()
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
                with open('page.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)
                print('file save')

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def get_result():
    offers = []
    with open('data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    #
    # with open('page.html', 'r', encoding='utf-8') as file:
    #     products_data = file.read()
    # soup = BeautifulSoup(products_data, 'lxml')
    # soup_datetexts = soup.find_all('span', class_='tooltip-target-wrapper-mu94t')
    # datetexts = soup_datetexts.find_all('div class', class_='date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs')

    # for datetext in soup_datetexts:
    #     if 'data-marker' in datetext:
    # time_offer = datetext['div class']

    # print(datetext)
    for key in json_data:
        if 'single-page' in key:
            for item in json_data[key]['data']['recommendationsInfinite']['items']:
                offer = {}
                offer['title'] = item['title']
                offer['price'] = item['priceDetailed']['value']
                offer['postfix'] = item['priceDetailed']['postfix']
                offer['location'] = item['location']['name']
                offer['url'] = 'https://www.avito.ru' + item['urlPath']
                # offer['data_time'] = item['value']['iva']['BadgeBarStep']['DateInfoStep']['payload']['absolute']
                offers.append(offer)
    # print(offers)

    for key in json_data:
        if 'single-page' in key:
            for item in json_data[key]['data']['vertical-widgets'][2:]:

                if type(item['value'].get('items')) != type(None):

                    data_times = item['value'].get('items')

                    for absolute in data_times:
                        absolute_t = absolute['value']['iva']['DateInfoStep']
                        for i in absolute_t:
                            try:
                                print(i['payload']['absolute'])
                                print(i['payload']['debug'].get('id'))
                            except Exception as ex:
                                print(ex)


if __name__ == '__main__':
    # url = 'https://www.avito.ru/barnaul/nedvizhimost?cd=1'
    # get_source_html(url)
    get_result()
