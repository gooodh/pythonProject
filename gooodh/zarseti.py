from fake_useragent import UserAgent
import requests
import datetime
from bs4 import BeautifulSoup

cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
ua = UserAgent()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': ua.random
}
link = 'https://www.zarseti.ru/Home'
try:
    response = requests.get(url=link, headers=headers).text

    soup = BeautifulSoup(response, 'lxml')
    data_g = soup.find('div', class_='Blackouts').text
    print(data_g)
except:
    print('нет оключений сегодня')
