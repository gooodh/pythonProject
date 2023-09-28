import requests
import json
import requests

cookies = {
    'PHPSESSID': 'f05531399e0bb51592ebbe342bfd7693',
    'ab_id': '3e765429028b87b45888b65ac1cdc17379a65aee',
    '_ga_7TF2BV73GT': 'GS1.1.1688617216.1.1.1688617231.0.0.0',
    '_ga': 'GA1.2.1073677447.1688617217',
    '_gid': 'GA1.2.1776082156.1688617218',
    '_gat_gtag_UA_179612189_1': '1',
    '_ym_uid': '1688617219571204022',
    '_ym_d': '1688617219',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=f05531399e0bb51592ebbe342bfd7693; ab_id=3e765429028b87b45888b65ac1cdc17379a65aee; _ga_7TF2BV73GT=GS1.1.1688617216.1.1.1688617231.0.0.0; _ga=GA1.2.1073677447.1688617217; _gid=GA1.2.1776082156.1688617218; _gat_gtag_UA_179612189_1=1; _ym_uid=1688617219571204022; _ym_d=1688617219; _ym_isad=2; _ym_visorc=w',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

response = requests.get('https://match-audio.ru/catalog/amplifiers', cookies=cookies, headers=headers)
with open('match-avto.html', 'w', encoding='utf-8') as file:
    # json.dump(response.json(), file, ensure_ascii=False)
    file.write(response.text)

