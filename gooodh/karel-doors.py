
from bs4 import BeautifulSoup

from datetime import datetime

import requests

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')

cookies = {
    'antibot_fc367ee9f4684e8b4df6ccf89e5a40d0': '2ccbe469c20c2be7550af6762ebb1293-1688695580',
    'PHPSESSID': 'd864cda011575903108931c8bbdc8193',
    'msfavorites': 'd864cda011575903108931c8bbdc8193',
    '_ga': 'GA1.1.1096260118.1688695584',
    '_ym_uid': '1688695586468663847',
    '_ym_d': '1688695586',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'antibot_hits': '13',
    '_ga_KJF9RKSWN8': 'GS1.1.1688695583.1.1.1688696122.0.0.0',
}

headers = {
    'authority': 'karel-doors.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'antibot_fc367ee9f4684e8b4df6ccf89e5a40d0=2ccbe469c20c2be7550af6762ebb1293-1688695580; PHPSESSID=d864cda011575903108931c8bbdc8193; msfavorites=d864cda011575903108931c8bbdc8193; _ga=GA1.1.1096260118.1688695584; _ym_uid=1688695586468663847; _ym_d=1688695586; _ym_isad=2; _ym_visorc=w; antibot_hits=13; _ga_KJF9RKSWN8=GS1.1.1688695583.1.1.1688696122.0.0.0',
    'referer': 'https://karel-doors.ru/iz-massiva-dereva/dveri-iz-massiva-sosny/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'page': '2',
}


def get_source_html():
    response = requests.get(
        'https://karel-doors.ru/mezhkomnatnye-dveri-ot-proizvoditelya/',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    with open('karel-doors.html', 'w', encoding='utf-8') as file:
        # json.dump(response.json(), file, ensure_ascii=False)
        file.write(response.text)


def get_result():
    # title_l=[]
    # price_l=[]
    # description_l=[]
    # link_l=[]
    with open('karel-doors.html', encoding='utf-8') as file:
        src = file.read()
    # with open(f'avito{cur_time}.csv', 'w', encoding='utf-8', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(
    #         [
    #                 'title',
    #                 'price',
    #                 'description',
    #                 'link',
    #             ]
            # )

    soup = BeautifulSoup(src, 'lxml')
    items = soup.find_all("div", class_="title__product")
    for i in items:
        print(i.text)

if __name__ == '__main__':

    # get_source_html()
    get_result()

