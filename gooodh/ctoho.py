import requests
import json




cookies = {
    'ses101hru': '037822a22784c7d5921788d324e55284eb97f041a732346b9fe2c7a35211dcc981a32ee38e1f87b675b230a14c733374c2d90d1547c7fd464f53fd7cef60c8276Efna5kotuckuY4oOT6FqRjKqqSYnwxfXmTY4jlW0id4mWILpYgyqgMa0M3cn2QyBMLgmf9BlPI2pwpniqnv%2BB2K3AYT0%2Bzohl4eN3Cly5meww92u7wGX07jvNXOWy%2BheUme6NUPW4karWKI0D%2BuimFN0jz21vzD6gPhPwct4QOz40eULyqM%2FH6JXZ63CVnBfIukslS2JzFb999X91Npc9WN%2FzyXAGC%2Fems0ULcdgxYCXernOMAnmcuP7RcU%2F2X6dxd7Qvx4y5v9h4iVvW7qKLfWSu0HRvZwVz2Yv7puVRNCvCgoNuxEbg4YhNgddT5Knn9p0Hmm0OotU8aVyGvrg44DlWK7iUWpdM%2FfVclYE%2BeG%2BByJ0KH7vq7hIC5xtWspyOm9rqE1tAj6y3CtBXTdQV6Lzb6XZRDWe1mMwSN%2FgfZL0NCGn9fsi6%2Fw4Cq52S94ywFkIQbIJhoQ7DI56vIO6g%3D%3D',
    'h101_original_referrer': 'kwork.ru',
    'h101dc': '2',
    'h101dcutm': '%5B%5D',
    'h101dcts': '1677588161',
    'h101dcparams': '%5B%5D',
    '_ga': 'GA1.1.1044674307.1677588165',
    '_ym_uid': '1677588165574065928',
    '_ym_d': '1677588165',
    'splitTest_uniformity_hotel': 'b',
    '_gid': 'GA1.2.386226531.1677747211',
    '_ym_isad': '2',
    'lvh': '570931',
    '_ym_visorc': 'b',
    '_currency_': 'RUB',
    '_searchparams_': '%7B%22in%22%3A%2201.06.2023%22%2C%22out%22%3A%2208.06.2023%22%2C%22adults%22%3A1%2C%22children%22%3A%5B%5D%2C%22prev_city_id%22%3A%2229%22%7D',
    '_filterparams_': 'null',
    'last_viewed_city': '29',
    'splitTest_uniformity_city': 'b',
    '_ga_NLYLJBVHVD': 'GS1.1.1677747389.1.1.1677747486.0.0.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://101hotels.com/main/cities/sochi?viewType=list&page=1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': 'ses101hru=037822a22784c7d5921788d324e55284eb97f041a732346b9fe2c7a35211dcc981a32ee38e1f87b675b230a14c733374c2d90d1547c7fd464f53fd7cef60c8276Efna5kotuckuY4oOT6FqRjKqqSYnwxfXmTY4jlW0id4mWILpYgyqgMa0M3cn2QyBMLgmf9BlPI2pwpniqnv%2BB2K3AYT0%2Bzohl4eN3Cly5meww92u7wGX07jvNXOWy%2BheUme6NUPW4karWKI0D%2BuimFN0jz21vzD6gPhPwct4QOz40eULyqM%2FH6JXZ63CVnBfIukslS2JzFb999X91Npc9WN%2FzyXAGC%2Fems0ULcdgxYCXernOMAnmcuP7RcU%2F2X6dxd7Qvx4y5v9h4iVvW7qKLfWSu0HRvZwVz2Yv7puVRNCvCgoNuxEbg4YhNgddT5Knn9p0Hmm0OotU8aVyGvrg44DlWK7iUWpdM%2FfVclYE%2BeG%2BByJ0KH7vq7hIC5xtWspyOm9rqE1tAj6y3CtBXTdQV6Lzb6XZRDWe1mMwSN%2FgfZL0NCGn9fsi6%2Fw4Cq52S94ywFkIQbIJhoQ7DI56vIO6g%3D%3D; h101_original_referrer=kwork.ru; h101dc=2; h101dcutm=%5B%5D; h101dcts=1677588161; h101dcparams=%5B%5D; _ga=GA1.1.1044674307.1677588165; _ym_uid=1677588165574065928; _ym_d=1677588165; splitTest_uniformity_hotel=b; _gid=GA1.2.386226531.1677747211; _ym_isad=2; lvh=570931; _ym_visorc=b; _currency_=RUB; _searchparams_=%7B%22in%22%3A%2201.06.2023%22%2C%22out%22%3A%2208.06.2023%22%2C%22adults%22%3A1%2C%22children%22%3A%5B%5D%2C%22prev_city_id%22%3A%2229%22%7D; _filterparams_=null; last_viewed_city=29; splitTest_uniformity_city=b; _ga_NLYLJBVHVD=GS1.1.1677747389.1.1.1677747486.0.0.0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'r': '0.5070129646711568',
    'params': '{"city_ids":[29],"hotel_ids":[],"destination":{},"search_by_date":1}',
}
def get_source_html():
    response = requests.get('https://101hotels.com/api/hotel/search', params=params, cookies=cookies, headers=headers)
    with open(f'ctohot.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False)

urls=[]
def get_result():

    with open('ctohot.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    for item in json_data['response']['hotels']:
        urls.append(item['url'])
    
    print(urls)


if __name__ == '__main__':
   
    # get_source_json()
    get_result()