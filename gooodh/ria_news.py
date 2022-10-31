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


def scap_news():
    response = requests.get(url=link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    soup_headers = soup.find_all('span', class_='share')

    with open(f'../rianews.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                'Статья',
                'Url'
            ]
        )

    for header in soup_headers:
        title_new = header['data-title']
        url_new = header['data-url']

        with open(f'../rianews.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    title_new,
                    url_new
                ]
            )

    print('Фаил rianews.csv создан')
if __name__ == '__main__':
    scap_news()