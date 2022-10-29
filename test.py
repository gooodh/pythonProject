from fake_useragent import UserAgent
import requests
import datetime
from time import sleep
import random
from bs4 import BeautifulSoup
import csv

cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'
}
link = 'https://2gis.ru/barnaul/search/%D0%90%D0%B2%D1%82%D0%BE%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81'

sess = requests.Session()
sess.get(link)
cookies = sess.get('https://2gis.ru/cookies')
sleep(random.randrange(2, 4))
response = sess.get(url=link, headers=headers, cookies=cookies).text
with open(f'index.html', 'w', encoding='utf-8') as file:
    file.write(response)
