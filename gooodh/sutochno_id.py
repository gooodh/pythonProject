import requests
import json

cookies = {
    'x-request-id': 'be612ab638559bd733faf8a9b36d04a9',
    'rid': 'be612ab638559bd733faf8a9b36d04a9',
    'route': '1677478825.052.60.51232|cb1faa23db9e30603aef3c84465716e1',
    'PHPSESSID': '6f50a9476d7e6fbf3350ead4d02e6bab',
    'language_id': 'ru',
    'x-request-id': 'd63b77bceed459b1764a07438920a2c7',
    'rid': 'd63b77bceed459b1764a07438920a2c7',
    'select_guests': '%7B%22guests%22%3A%7B%22adults%22%3A2%2C%22childrens%22%3A%5B%5D%7D%7D',
    '_me_': 'fB36QnKDuLeFMyeSN3Gwgg',
    '_gcl_au': '1.1.637749176.1677478825',
    '_ga_QFVTBCKP86': 'GS1.1.1677478825.1.1.1677482115.56.0.0',
    '_ga': 'GA1.1.2128120006.1677478826',
    '_gid': 'GA1.2.1351776290.1677478827',
    '_ym_uid': '1677478827247410997',
    '_ym_d': '1677478827',
    'tmr_lvid': 'd441844c2b07aeb620a8dc3d2fb1149c',
    'tmr_lvidTS': '1677478827796',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1677482039879',
    'calendar_dates': '%7B%22date_begin%22%3A%222023-02-28%22%2C%22date_end%22%3A%222023-03-01%22%7D',
    '_ym_visorc': 'b',
    '_ia_': '0',
    'objects_views': '1292957',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://sutochno.ru/front/searchapp/detail/1292957?guests_adults=2&occupied=2023-02-28;2023-03-01&id=1&SW.lat=43.60050204053169&SW.lng=39.711769219512924&NE.lat=43.60817371320619&NE.lng=39.72872078048705',
    'api-version': '1.10',
    'platform': 'js',
    'token': 'Hy6U3z61fflbgT2yJ/VdlQ2719',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Alt-Used': 'sutochno.ru',
    # 'Cookie': 'x-request-id=be612ab638559bd733faf8a9b36d04a9; rid=be612ab638559bd733faf8a9b36d04a9; route=1677478825.052.60.51232|cb1faa23db9e30603aef3c84465716e1; PHPSESSID=6f50a9476d7e6fbf3350ead4d02e6bab; language_id=ru; x-request-id=d63b77bceed459b1764a07438920a2c7; rid=d63b77bceed459b1764a07438920a2c7; select_guests=%7B%22guests%22%3A%7B%22adults%22%3A2%2C%22childrens%22%3A%5B%5D%7D%7D; _me_=fB36QnKDuLeFMyeSN3Gwgg; _gcl_au=1.1.637749176.1677478825; _ga_QFVTBCKP86=GS1.1.1677478825.1.1.1677482115.56.0.0; _ga=GA1.1.2128120006.1677478826; _gid=GA1.2.1351776290.1677478827; _ym_uid=1677478827247410997; _ym_d=1677478827; tmr_lvid=d441844c2b07aeb620a8dc3d2fb1149c; tmr_lvidTS=1677478827796; _ym_isad=2; tmr_detect=0%7C1677482039879; calendar_dates=%7B%22date_begin%22%3A%222023-02-28%22%2C%22date_end%22%3A%222023-03-01%22%7D; _ym_visorc=b; _ia_=0; objects_views=1292957',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'id': '1292957',
    'currency_id': '1',
}

response = requests.get('https://sutochno.ru/api/json/objects/getObject', params=params, cookies=cookies, headers=headers)


with open(f'sutochno_id.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)