# from fake_useragent import UserAgent
import requests
import datetime
from bs4 import BeautifulSoup
import csv


cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
# ua = UserAgent()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
link = 'https://tvoy-bizness.ru/stroitel-stvo-domov-pod-klyuch-2/'

response = requests.get(url=link, headers=headers).text

soup = BeautifulSoup(response, 'lxml')


data_g = soup.find('div', class_='entry post clearfix')

title = data_g.find('h1', class_="title").text
contents = data_g.find_all('p')
contents=contents[:-1]
content2 =''
for content in contents:
    content = content.text.strip()
    content2 += content
with open(f'tvoy-bizness_{title}.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
            [
                    'title',
                    'content',
                    
                ]
            )
with open(f'tvoy-bizness_{title}.csv', 'a', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)

    writer.writerow(
                [
                    title,
                    content2
                ]
            )
