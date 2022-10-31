import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
import random


def image_data():
    image_number = 1
    link = f'https://zastavok.net'

    ua = UserAgent()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    for store_number in range(2, 2688):

        resource = requests.get(f'{link}/{store_number}', headers=headers).text
        soup = BeautifulSoup(resource, 'lxml')
        block = soup.find('div', class_='block-photo')
        all_image = block.find_all('div', class_='short_full')
        for image in all_image:
            image_link = image.find('a').get('href')
            download_storage = requests.get(f'{link}{image_link}').text
            download_soup = BeautifulSoup(download_storage, 'lxml')
            download_block = download_soup.find('div', class_='block_down')
            result_link = download_block.find('a').get('href')
            image_bytes = requests.get(f'{link}{result_link}').content
            with open(f'image/{image_number}.jpg', 'wb') as file:
                file.write(image_bytes)
            image_number += 1
            print(image_number)
            sleep(random.randrange(2, 4))



if __name__ == '__main__':
    image_data()
