
from bs4 import BeautifulSoup

from datetime import datetime

import requests

cookies = {
    'PHPSESSID': 'd7e7d6409539a78c7eedef22cdf57e92',
    'check_cookie_eu': '1',
    'prian_hash': '303592ed0891c52defa1f2ea40061346',
    'search_view': '2',
    'tmr_lvid': '4196078276de598c0f735fbfe4f802cd',
    'tmr_lvidTS': '1688716315147',
    'request_error_type': 'none',
    'request_form_send': 'yes',
    '_ym_uid': '1688716316294820320',
    '_ym_d': '1688716316',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_gid': 'GA1.2.1202210863.1688716317',
    '__cf_bm': 'KaSM0Hbxvht6qy8SXrr0NmPyR.eXhUEkm0ER99_W2Fg-1688716317-0-AaHwZvbqlP6c1F/ct2cGxN4SUMjOaQBSdoNGTJ1EwLEIfx6t/fNaFT/q/KYnAwquZg==',
    '_ga_84EWRFG227': 'GS1.1.1688716317.1.1.1688716399.0.0.0',
    '_ga_E3YL8SE1HX': 'GS1.1.1688716317.1.1.1688716400.57.0.0',
    '_ga': 'GA1.1.1011573089.1688716317',
    'tmr_detect': '0%7C1688716402701',
    'agree_cookie_warning': '1',
}

headers = {
    'authority': 'prian.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'PHPSESSID=d7e7d6409539a78c7eedef22cdf57e92; check_cookie_eu=1; prian_hash=303592ed0891c52defa1f2ea40061346; search_view=2; tmr_lvid=4196078276de598c0f735fbfe4f802cd; tmr_lvidTS=1688716315147; request_error_type=none; request_form_send=yes; _ym_uid=1688716316294820320; _ym_d=1688716316; _ym_isad=2; _ym_visorc=b; _gid=GA1.2.1202210863.1688716317; __cf_bm=KaSM0Hbxvht6qy8SXrr0NmPyR.eXhUEkm0ER99_W2Fg-1688716317-0-AaHwZvbqlP6c1F/ct2cGxN4SUMjOaQBSdoNGTJ1EwLEIfx6t/fNaFT/q/KYnAwquZg==; _ga_84EWRFG227=GS1.1.1688716317.1.1.1688716399.0.0.0; _ga_E3YL8SE1HX=GS1.1.1688716317.1.1.1688716400.57.0.0; _ga=GA1.1.1011573089.1688716317; tmr_detect=0%7C1688716402701; agree_cookie_warning=1',
    'referer': 'https://prian.ru/search/?where[1]=%D0%A2%D1%83%D1%80%D1%86%D0%B8%D1%8F&acountry[1]=38&type[]=1&search_currency=2&next=30',
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



def get_source_html():
    response = requests.get(
        'https://prian.ru/search/?where[1]=%D0%A2%D1%83%D1%80%D1%86%D0%B8%D1%8F&acountry[1]=38&type[]=1&search_currency=2&next=60',
        cookies=cookies,
        headers=headers,
    )

    with open('prian.html', 'w', encoding='utf-8') as file:
        # json.dump(response.json(), file, ensure_ascii=False)
        file.write(response.text)


def get_result():
    # title_l=[]
    # price_l=[]
    # description_l=[]
    # link_l=[]
    with open('prian.html', encoding='utf-8') as file:
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
    titles = soup.find_all("div", class_="b-title")
    links = soup.find_all("a", href=True)
    for link in links:
        lin = link['href'].split('/')
        if len(lin) >= 5:
            if lin[3] in 'price':
                if not lin[4] in 'contact':
                    print(link['href'])


if __name__ == '__main__':

    # get_source_html()
    get_result()
