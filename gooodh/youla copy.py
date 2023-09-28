import requests
import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Youla-Json': '{}',
    'X-Youla-Splits': '8a=3|8b=5|8c=0|8m=0|8v=0|8z=0|16a=0|16b=0|64a=2|64b=0|100a=40|100b=81|100c=0|100d=0|100m=0',
    'X-Offset-UTC': '+07:00',
    'Origin': 'https://youla.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://youla.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = {
    'app_id': 'web/3',
    'uid': '63fc6ff2c7a8c',
    'timestamp': '1677488962155',
}

response = requests.get('https://api.youla.io/api/v1/product/61e5df7ea5874b554e4dc58b/similars', params=params, headers=headers)

with open(f'youla.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)