import requests

cookies = {
    'PHPSESSID': 'gUF4wehrus0frgz4KYG9kEZxn22ZtcMY',
    'user_cart': 'a%3A0%3A%7B%7D',
    '_ym_uid': '1681823968982116427',
    '_ym_d': '1681823968',
    'BX_USER_ID': 'f3b56d53fa8fff5403f3ffbf6dc91119',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://moskva-kovka.ru/catalog/)',
    # 'Cookie': 'PHPSESSID=gUF4wehrus0frgz4KYG9kEZxn22ZtcMY; user_cart=a%3A0%3A%7B%7D; _ym_uid=1681823968982116427; _ym_d=1681823968; BX_USER_ID=f3b56d53fa8fff5403f3ffbf6dc91119; _ym_isad=2; _ym_visorc=w',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://moskva-kovka.ru/catalog/kovanye-balkony/', cookies=cookies, headers=headers)

with open('kovka.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
