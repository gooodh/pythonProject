import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Origin': 'https://www.bankturov.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bankturov.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'departure': '1',
    'destination': [
        '9',
    ],
    'adults': '3',
    'children': [
        '12',
        '10',
        '1',
    ],
    'date': {
        'from': '09.05.2023',
        'till': '09.05.2023',
    },
    'nights': {
        'from': '7',
        'till': '14',
    },
    'stars': [
        1,
        2,
        3,
        4,
        5,
    ],
    'hotels': [],
    'resorts': [],
    'subResorts': [],
    'mealType': 1,
    'hotelStatus': False,
    'minCost': 0,
    'maxCost': 99999999,
    'sourceCurrency': 'RUB',
    'offerCurrency': 'RUB',
    'source': 'search_online_page',
    'cid': 1,
    'page': 1,
    'hotels_count': 0,
    'results_count': 0,
    'firstCoastline': False,
    'debug': 0,
}

response = requests.post('https://search.bankturov.ru/api/v3/search', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"departure":"1","destination":["9"],"adults":"3","children":["12","10","1"],"date":{"from":"09.05.2023","till":"09.05.2023"},"nights":{"from":"7","till":"14"},"stars":[1,2,3,4,5],"hotels":[],"resorts":[],"subResorts":[],"mealType":1,"hotelStatus":false,"minCost":0,"maxCost":99999999,"sourceCurrency":"RUB","offerCurrency":"RUB","source":"search_online_page","cid":1,"page":1,"hotels_count":0,"results_count":0,"firstCoastline":false,"debug":0}'
#response = requests.post('https://search.bankturov.ru/api/v3/search', headers=headers, data=data)

with open(f'bankturov.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)