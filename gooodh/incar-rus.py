

import requests

cookies = {
    'PHPSESSID': 'dc058d63b9060455c950b88aafffc239',
    'BITRIX_SM_SALE_UID': 'b82f43de5a831dadb7291fc94210f962',
    '_ym_debug': 'null',
    '_ga_6PWJR49LCK': 'GS1.1.1688627483.1.1.1688627841.0.0.0',
    '_ga': 'GA1.1.867104946.1688627484',
    'BX_USER_ID': 'c5c43b286ae0b5ba8da6db339e6800bc',
    '_ym_uid': '1688627493437815134',
    '_ym_d': '1688627493',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A18%2C%22EXPIRE%22%3A1688677140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://incar-rus.ru/catalog/shtatnaya-magnitola/search/?marka_id=&model_id=&year_id=',
    # 'Cookie': 'PHPSESSID=dc058d63b9060455c950b88aafffc239; BITRIX_SM_SALE_UID=b82f43de5a831dadb7291fc94210f962; _ym_debug=null; _ga_6PWJR49LCK=GS1.1.1688627483.1.1.1688627841.0.0.0; _ga=GA1.1.867104946.1688627484; BX_USER_ID=c5c43b286ae0b5ba8da6db339e6800bc; _ym_uid=1688627493437815134; _ym_d=1688627493; _ym_isad=2; _ym_visorc=w; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A18%2C%22EXPIRE%22%3A1688677140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

params = {
    'marka_id': '',
    'model_id': '',
    'year_id': '',
    'PAGEN_1': '3',
}

response = requests.get(
    'https://incar-rus.ru/catalog/shtatnaya-magnitola/search/',
    params=params,
    cookies=cookies,
    headers=headers,
)


response = requests.get(
    'https://incar-rus.ru/catalog/shtatnaya-magnitola/search/',
    params=params,
    cookies=cookies,
    headers=headers,
)
with open('incar-rus.html', 'w', encoding='utf-8') as file:
    # json.dump(response.json(), file, ensure_ascii=False)
    file.write(response.text)

