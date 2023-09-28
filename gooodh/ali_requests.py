
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')


import requests

cookies = {
    'xman_us_f': 'x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=8bb967990d084996a976e0d42197b151',
    'acs_usuc_t': 'x_csrf=1ddg3o7j81dch&acs_rt=8127922d61514b9b815954792bf8f117',
    'aep_usuc_f': 'site=rus&c_tp=RUB&region=RU&b_locale=ru_RU',
    'xman_t': 'DSOKlACGc5q7rRIz+FoZ+yFMeDYACcPFQ7xxVXB59x90AX6uhOJE0pCaAyHP1iuM',
    'xman_f': 'JbNm0KqoWjlABG3kPq0ZHhr9RtxwV5m5f/c9kV1T09RCso8cxt++rRovCLdYtRIX63AjkaBjCHRNUaPp5gUb+wp8FbqU47Xv7IgI+ZBnvpv1HjP9kQ8j3w==',
    'intl_locale': 'ru_RU',
    'intl_common_forever': 'xV4yuljKYqvx+EPpFDTd12nNF4SAWDBYceMkkE80OYRMDxr5jinYzg==',
    'JSESSIONID': '6AB59F70EE797C79745CB0CF593F922F',
    'aer_abid': '323c1b5af8e865e0',
    'l': 'fBIomPNqTvumSnRwBO5BFurza77O6IR44kPzaNbMiIEGC6UhZf99b-RQmOzUoKxRRBX5tK8e4fQxxgp9-etFs9DXACsBQPWdpxDDBeYB4',
    'tfstk': 'cndGBNZMD84jXgYNdh1sZfzf8v9ca4zNfTBeT2MDJ5VFmlvC8sfLL8k_BlsEVcyf.',
    'isg': 'BEREOM7d-84p-0-C4L_feWe8Fss2XWjHXznwmF7lL47vieRThW8RVk5nyblRiqAf',
    'xlly_s': '1',
    'cna': 'bNyAHGDxrUICASVwvr3L3/rt',
    'tmr_lvid': 'a515c24f5c3d6b35f0bfcc8c05e45ddf',
    'tmr_lvidTS': '1677323884991',
    '_ga': 'GA1.2.582046947.1677323885',
    '_gid': 'GA1.2.1390144403.1677323885',
    '_ym_uid': '1677323886275541837',
    '_ym_d': '1677323886',
    '_ym_isad': '2',
    '_fbp': 'fb.1.1677323887094.466335825',
    '_ym_visorc': 'b',
    'tmr_detect': '0%7C1677324897667',
    'ae_ru_pp_v': '1.0.2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://aliexpress.ru/category/202000006/computer-office.html?g=n&page=8&spm=a2g2w.productlist.categorylist.3.2bd94aa6Qy3FSi',
    'content-type': 'application/json',
    'bx-v': '2.2.3',
    'Origin': 'https://aliexpress.ru',
    'Connection': 'keep-alive',
    # 'Cookie': 'xman_us_f=x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=8bb967990d084996a976e0d42197b151; acs_usuc_t=x_csrf=1ddg3o7j81dch&acs_rt=8127922d61514b9b815954792bf8f117; aep_usuc_f=site=rus&c_tp=RUB&region=RU&b_locale=ru_RU; xman_t=DSOKlACGc5q7rRIz+FoZ+yFMeDYACcPFQ7xxVXB59x90AX6uhOJE0pCaAyHP1iuM; xman_f=JbNm0KqoWjlABG3kPq0ZHhr9RtxwV5m5f/c9kV1T09RCso8cxt++rRovCLdYtRIX63AjkaBjCHRNUaPp5gUb+wp8FbqU47Xv7IgI+ZBnvpv1HjP9kQ8j3w==; intl_locale=ru_RU; intl_common_forever=xV4yuljKYqvx+EPpFDTd12nNF4SAWDBYceMkkE80OYRMDxr5jinYzg==; JSESSIONID=6AB59F70EE797C79745CB0CF593F922F; aer_abid=323c1b5af8e865e0; l=fBIomPNqTvumSnRwBO5BFurza77O6IR44kPzaNbMiIEGC6UhZf99b-RQmOzUoKxRRBX5tK8e4fQxxgp9-etFs9DXACsBQPWdpxDDBeYB4; tfstk=cndGBNZMD84jXgYNdh1sZfzf8v9ca4zNfTBeT2MDJ5VFmlvC8sfLL8k_BlsEVcyf.; isg=BEREOM7d-84p-0-C4L_feWe8Fss2XWjHXznwmF7lL47vieRThW8RVk5nyblRiqAf; xlly_s=1; cna=bNyAHGDxrUICASVwvr3L3/rt; tmr_lvid=a515c24f5c3d6b35f0bfcc8c05e45ddf; tmr_lvidTS=1677323884991; _ga=GA1.2.582046947.1677323885; _gid=GA1.2.1390144403.1677323885; _ym_uid=1677323886275541837; _ym_d=1677323886; _ym_isad=2; _fbp=fb.1.1677323887094.466335825; _ym_visorc=b; tmr_detect=0%7C1677324897667; ae_ru_pp_v=1.0.2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    '_bx-v': '2.2.3',
}

json_data = {
    'catId': '202000006',
    'g': 'n',
    'storeIds': [],
    'page': 8,
    'searchInfo': 'category:eyJ0aXRsZSI6ItCa0L7QvNC/0YzRjtGC0LXRgNGLINC4INC+0YTQuNGBIiwic2x1ZyI6ImNvbXB1dGVyLW9mZmljZSIsImxlYWYiOmZhbHNlLCJpZCI6IjIwMjAwMDAwNiIsInNlbGxlckNhdGVnb3J5SWQiOiIyMDE2MDU1MDMiLCJ0cmVlVHlwZSI6Im9sZCJ9',
}



# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"catId":"202000006","g":"n","storeIds":[],"page":8,"searchInfo":"category:eyJ0aXRsZSI6ItCa0L7QvNC/0YzRjtGC0LXRgNGLINC4INC+0YTQuNGBIiwic2x1ZyI6ImNvbXB1dGVyLW9mZmljZSIsImxlYWYiOmZhbHNlLCJpZCI6IjIwMjAwMDAwNiIsInNlbGxlckNhdGVnb3J5SWQiOiIyMDE2MDU1MDMiLCJ0cmVlVHlwZSI6Im9sZCJ9"}'
#response = requests.post(
#    'https://aliexpress.ru/aer-jsonapi/v1/category_filter',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)
def get_source_html():
    response = requests.post(
    'https://aliexpress.ru/aer-jsonapi/v1/category_filter',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
    with open(f'ali.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False)


def get_result():
    title_l=[]
    price_l=[]
    description_l=[]
    link_l=[]
    with open('avito.html', encoding='utf-8') as file:
        src = file.read()

    with open(f'avito{cur_time}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                    'title',
                    'price',
                    'description',
                    'link',
                ]
            )
    soup = BeautifulSoup(src, 'lxml')
    items = soup.find_all("div", class_="iva-item-titleStep-pdebR")
    pricesteps = soup.find_all('div', class_= 'iva-item-priceStep-uq2CQ')
    descriptions = soup.find_all('div', class_='iva-item-descriptionStep-C0ty1')

    for d in descriptions:
        description = d.find('div', class_= 'iva-item-text-Ge6dR').text.strip()
        description_l.append(description)
       

    for p in pricesteps:
        price = p.find('span', class_= 'price-root-RA1pj').text.strip()
        price_l.append(price)
        
       
    for i in items:
        title = i.find('h3', class_='title-root-zZCwT').text.strip()
        link = 'https://www.avito.ru' + i.find('a').get('href')
        link_l.append(link)
        title_l.append(title)

    rows = zip(title_l, price_l, description_l, link_l)
        
    with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':
   
    get_source_html()
    # get_result()

