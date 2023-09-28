
from bs4 import BeautifulSoup
import csv

import requests


cookies = {
    'ses101hru': '037822a22784c7d5921788d324e55284eb97f041a732346b9fe2c7a35211dcc981a32ee38e1f87b675b230a14c733374c2d90d1547c7fd464f53fd7cef60c8276Efna5kotuckuY4oOT6FqRjKqqSYnwxfXmTY4jlW0id4mWILpYgyqgMa0M3cn2QyBMLgmf9BlPI2pwpniqnv%2BB2K3AYT0%2Bzohl4eN3Cly5meww92u7wGX07jvNXOWy%2BheUme6NUPW4karWKI0D%2BuimFN0jz21vzD6gPhPwct4QOz40eULyqM%2FH6JXZ63CVnBfIukslS2JzFb999X91Npc9WN%2FzyXAGC%2Fems0ULcdgxYCXernOMAnmcuP7RcU%2F2X6dxd7Qvx4y5v9h4iVvW7qKLfWSu0HRvZwVz2Yv7puVRNCvCgoNuxEbg4YhNgddT5Knn9p0Hmm0OotU8aVyGvrg44DlWK7iUWpdM%2FfVclYE%2BeG%2BByJ0KH7vq7hIC5xtWspyOm9rqE1tAj6y3CtBXTdQV6Lzb6XZRDWe1mMwSN%2FgfZL0NCGn9fsi6%2Fw4Cq52S94ywFkIQbIJhoQ7DI56vIO6g%3D%3D',
    'h101_original_referrer': 'kwork.ru',
    'h101dc': '2',
    'h101dcutm': '%5B%5D',
    'h101dcts': '1677588161',
    'h101dcparams': '%5B%5D',
    '_ga': 'GA1.2.1044674307.1677588165',
    '_ym_uid': '1677588165574065928',
    '_ym_d': '1677588165',
    'splitTest_uniformity_hotel': 'b',
    '_gid': 'GA1.2.386226531.1677747211',
    '_currency_': 'RUB',
    '_searchparams_': '%7B%22prev_city_id%22%3A%2229%22%2C%22adults%22%3A%221%22%2C%22in%22%3A%2201.06.2023%22%2C%22out%22%3A%2202.06.2023%22%7D',
    'last_viewed_city': '29',
    'splitTest_uniformity_city': 'b',
    '_ga_NLYLJBVHVD': 'GS1.1.1677824171.3.1.1677826216.0.0.0',
    '_filterparams_': 'null',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'lvh': '657259',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'ses101hru=037822a22784c7d5921788d324e55284eb97f041a732346b9fe2c7a35211dcc981a32ee38e1f87b675b230a14c733374c2d90d1547c7fd464f53fd7cef60c8276Efna5kotuckuY4oOT6FqRjKqqSYnwxfXmTY4jlW0id4mWILpYgyqgMa0M3cn2QyBMLgmf9BlPI2pwpniqnv%2BB2K3AYT0%2Bzohl4eN3Cly5meww92u7wGX07jvNXOWy%2BheUme6NUPW4karWKI0D%2BuimFN0jz21vzD6gPhPwct4QOz40eULyqM%2FH6JXZ63CVnBfIukslS2JzFb999X91Npc9WN%2FzyXAGC%2Fems0ULcdgxYCXernOMAnmcuP7RcU%2F2X6dxd7Qvx4y5v9h4iVvW7qKLfWSu0HRvZwVz2Yv7puVRNCvCgoNuxEbg4YhNgddT5Knn9p0Hmm0OotU8aVyGvrg44DlWK7iUWpdM%2FfVclYE%2BeG%2BByJ0KH7vq7hIC5xtWspyOm9rqE1tAj6y3CtBXTdQV6Lzb6XZRDWe1mMwSN%2FgfZL0NCGn9fsi6%2Fw4Cq52S94ywFkIQbIJhoQ7DI56vIO6g%3D%3D; h101_original_referrer=kwork.ru; h101dc=2; h101dcutm=%5B%5D; h101dcts=1677588161; h101dcparams=%5B%5D; _ga=GA1.2.1044674307.1677588165; _ym_uid=1677588165574065928; _ym_d=1677588165; splitTest_uniformity_hotel=b; _gid=GA1.2.386226531.1677747211; _currency_=RUB; _searchparams_=%7B%22prev_city_id%22%3A%2229%22%2C%22adults%22%3A%221%22%2C%22in%22%3A%2201.06.2023%22%2C%22out%22%3A%2202.06.2023%22%7D; last_viewed_city=29; splitTest_uniformity_city=b; _ga_NLYLJBVHVD=GS1.1.1677824171.3.1.1677826216.0.0.0; _filterparams_=null; _ym_isad=2; _ym_visorc=b; lvh=657259',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}



sity = 'sochi'

url = f'https://101hotels.com/main/cities/{sity}/otel_le_rond_sochi_resortspa.html'
def get_source_html():
    
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    # with open(f'stoh_id.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)
    get_result(response)

def get_result(response):
    # with open('stoh_id.html', encoding='utf-8') as file:
    #     src = file.read()

    soup = BeautifulSoup(response.text, 'lxml')
    # soup = BeautifulSoup(src, 'lxml')

    title = soup.find('h1', class_="hotel__header").text.strip()
    phone = soup.find('span', class_="hotel_phone__number").text.strip()
    address = soup.find('span', class_="hotel__address").text.strip()
    description = soup.find("div", {"id": "hotel"}).find('div', class_='hotel-description').find("div", {"id": "description"}).find('div', attrs={'style':"margin-right: 285px;"}).text.strip()
    price = soup.find('span', class_="price-value price-highlight rub").text.strip()
    link_l=[]
    gallery = soup.find('div', class_="hotel-gallery")
    for a in gallery.find_all('a', href=True):
        link = a['href']
        link_l.append(link)
    

    with open(f'stohot_{sity}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                    'Название объявления',
                    'Цена',
                    'Телефон',
                    'Описание',
                    'Категория, раздел',
                    'Url',
                    'Url_foto',
                ]
            )
    
    with open(f'stohot_{sity}.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
                [
                    title,
                    price,
                    phone,
                    description,
                    address,
                    url,
                    link_l
                ]
        )
if __name__ == '__main__':
   
    get_source_html()
    