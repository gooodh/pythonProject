import datetime
import csv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_data(city_code='2398'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()  # пример Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }
    response = requests.get(url='https://magnit.ru/promo/', headers=headers, cookies=cookies)
    # with open(f'index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)

    with open('index.html', encoding='utf-8') as file:
        src = file.read()

    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(src, 'lxml')


    city = soup.find('a', class_='header__contacts-link_city').text.strip()
    cards = soup.find_all('a', class_='card-sale_catalogue')
    print(city, len(cards))
    #     with open(f'{city}_{cur_time}.csv', 'w') as file:
    #         writer = csv.writer(file)
    #
    #         writer.writerow(
    #             [
    #                 'Продукт',
    #                 'Старая цена',
    #                 'Новая цена',
    #                 'Процент скидки',
    #                 'Время акции',
    #             ]
    #         )
    #
    data = []
    for card in cards:
        card_title = card.find('div', class_='card-sale__title').text.strip()
        print(card_title)
    #         try:
    #             card_discount = card.find('div', class_='card-sale__discount').text.strip()
    #         except AttributeError:
    #             continue
    #
    #         card_price_old_integer = card.find('div', class_='label__price_old').find('span',
    #                                                                                   class_='label__price-integer').text.strip()
    #         card_price_old_decimal = card.find('div', class_='label__price_old').find('span',
    #                                                                                   class_='label__price-decimal').text.strip()
    #         card_old_price = f'{card_price_old_integer}.{card_price_old_decimal}'
    #
    #         card_price_integer = card.find('div', class_='label__price_new').find('span',
    #                                                                               class_='label__price-integer').text.strip()
    #         card_price_decimal = card.find('div', class_='label__price_new').find('span',
    #                                                                               class_='label__price-decimal').text.strip()
    #         card_price = f'{card_price_integer}.{card_price_decimal}'
    #
    #         card_sale_date = card.find('div', class_='card-sale__date').text.strip().replace('\n', ' ')
    #
    #         data.append(
    #             [card_discount, card_old_price, card_price, card_sale_date]
    #         )
    #         # print(card_sale_date, card_price)
    #
    #         with open(f'{city}_{cur_time}.csv', 'a') as file:
    #             writer = csv.writer(file)
    #
    #             writer.writerow(
    #                 [
    #                     card_title,
    #                     card_old_price,
    #                     card_price,
    #                     card_discount,
    #                     card_sale_date,
    #                 ]
    #             )
    #
    #         print(f'Файл {city}_{cur_time}.csv успешно записан!')
    #
    #
    # # print(ua.random)




if __name__ == '__main__':
    collect_data()
