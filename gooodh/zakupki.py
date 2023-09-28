
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')

full_name = ''
address = ''
inn = ''


cookies = {
    'doNotAdviseToChangeLocationWhenIosReject': 'true',
    '_ym_uid': '1695799031944035738',
    '_ym_d': '1695799031',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'doNotAdviseToChangeLocationWhenIosReject=true; _ym_uid=1695799031944035738; _ym_d=1695799031; _ym_isad=2; _ym_visorc=b',
    'Referer': 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'morphology': 'on',
    'search-filter': 'Дате размещения',
    'pageNumber': '1',
    'sortDirection': 'false',
    'recordsPerPage': '_500',
    'showLotsInfoHidden': 'false',
    'sortBy': 'UPDATE_DATE',
    'fz223': 'on',
    'af': 'on',
    'ca': 'on',
    'pc': 'on',
    'pa': 'on',
    'currencyIdGeneral': '-1',
}


def get_source_html():
    response = requests.get(
        'https://zakupki.gov.ru/epz/order/extendedsearch/results.html',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    with open('zakupki.html', 'w', encoding='utf-8') as file:
        file.write(response.text)


search_links = []

with open('zakupki.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                    'full_name',
                    'address',
                    'inn',
                ]
            )


def get_result():
    with open('zakupki.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    block = soup.find_all('div', class_='registry-entry__body-href')
    for links in block:
        link = links.find('a').get('href')
        search_links.append(link)
    result()


def result():
    for links in search_links:
        response = requests.get(f'https://zakupki.gov.ru/{links}',
                                params=params,
                                cookies=cookies,
                                headers=headers,
                                )
        with open('result.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        result_csv(full_name, address, inn)


def result_csv(full_name, address, inn):

    with open('result.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    # block = soup.find_all('section', class_='blockInfo__section section')
    full_name = soup.find('div', class_='registry-entry__header-mid mt-4 align-items-center').find('div', class_='registry-entry__header-mid__number text-normal').text.strip()
    address = soup.find('div', class_='row no-gutters registry-entry__form m-0').find('div', class_='registry-entry__body-value').text.strip()
    inn = soup.find_all('div', class_='registry-entry__body-block')[1].find_all('div', class_='col-md-auto')[1].find('div', class_='registry-entry__body-value').text
   

    # for name in block:
    #     name = name.find('span', class_='section__title')
    #     if name.text in 'Полное наименование':
    #         full_name = name.next_element.next_element.next_element.text.strip()
    #     if name.text in 'Адрес (место нахождения)':
    #         address = name.next_element.next_element.next_element.text.strip()
    #     elif name.text in 'Место нахождения':
    #         address = name.next_element.next_element.next_element.text.strip()
    #     if name.text in 'ИНН':
    #         inn = name.next_element.next_element.next_element.text.strip()

    with open('zakupki.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
                        [
                            full_name,
                            address,
                            inn
                        ]
                    )
    print(full_name)

if __name__ == '__main__':
    # get_source_html()
    get_result()
    # result()
    # result_csv(full_name, address, inn)
