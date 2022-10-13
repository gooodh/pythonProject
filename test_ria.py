from fake_useragent import UserAgent
import requests
import datetime
from bs4 import BeautifulSoup
import csv

cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')

ua = UserAgent()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': ua.random
}
link = 'https://ria.ru/'
# link = 'http://httpbin.org/get'

response = requests.get(url=link, headers=headers).text

# print(response.raise_for_status)
# print(response.ok)
#
# with open(f'index.html', 'w', encoding='utf-8') as file:
#     file.write(response)

# with open('index.html', encoding='utf-8') as file:
#     src = file.read()

soup = BeautifulSoup(response, 'lxml')
headerss = soup.find_all('span', class_='share')
with open(f'rianews.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(
        [
            'Статья',
            'Url'
        ]
    )

for header in headerss:
    title_new = header['data-title']
    url_new = header['data-url']

    with open(f'rianews.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                title_new,
                url_new
            ]
        )

# try:
#     response = requests.get(url=link, headers=headers).text
#     status = requests.get(url=link, headers=headers).status_code
#
#     # soup = BeautifulSoup(response, 'lxml')
#     # data_g = soup.find('body', class_='body m-ria m-index-page m-header-sticked m-header-ready m-widget-lenta-active').text
#     # with open(f'index.html', 'w') as file:
#     #     file.write(response)
#
#     print(status)
# except:
#     print('нет оключений сегодня')
