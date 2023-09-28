
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')



cookies = {
    'session-id': '138-6538996-7828955',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'USD',
    'sp-cdn': '"L5Z9:RU"',
    'skin': 'noskin',
    'ubid-main': '135-1888967-8697109',
    'session-token': '"3OcjhuW341WhhXm3YQYeeolCpUulCim78Dofd8ieyGztQxHmK8E2f/7FG3+2gK34ih9/anG2Wk5FchvwXj00cR2DCle3YfRwsBWizI5DVqI9U01eBSQkmlfyGA0MMtuf74jW5Gn2gfSE+Ipz6p9KZxtxnNjHoDNkyxFnpAg7e1Xw5rELt1npBB3sHtOfMQR5xwpOqrIgOkdgI15z8O/lWhbWhKwhTZzBf13Mw4YWSno="',
    'csm-hit': 'tb:WDSX0Q1GQ2HSXNSCN9D2+s-WDSX0Q1GQ2HSXNSCN9D2|1688976736075&t:1688976736075&adb:adblk_no',
}

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'session-id=138-6538996-7828955; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:RU"; skin=noskin; ubid-main=135-1888967-8697109; session-token="3OcjhuW341WhhXm3YQYeeolCpUulCim78Dofd8ieyGztQxHmK8E2f/7FG3+2gK34ih9/anG2Wk5FchvwXj00cR2DCle3YfRwsBWizI5DVqI9U01eBSQkmlfyGA0MMtuf74jW5Gn2gfSE+Ipz6p9KZxtxnNjHoDNkyxFnpAg7e1Xw5rELt1npBB3sHtOfMQR5xwpOqrIgOkdgI15z8O/lWhbWhKwhTZzBf13Mw4YWSno="; csm-hit=tb:WDSX0Q1GQ2HSXNSCN9D2+s-WDSX0Q1GQ2HSXNSCN9D2|1688976736075&t:1688976736075&adb:adblk_no',
    'device-memory': '4',
    'downlink': '3.25',
    'dpr': '1',
    'ect': '4g',
    'rtt': '250',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-viewport-width': '706',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'viewport-width': '706',
}



def get_source_json():
    response = requests.get('https://www.amazon.com/dp/B07B94ZR74', cookies=cookies, headers=headers)
    with open('amazom_B07B94ZR74.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    # with open(f'amazom.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, ensure_ascii=False)

def get_result():

    with open('amazom_B07B94ZR74.html', 'r', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    # titles = soup.find_all("div", id_="ivLargeImage")
    # links = soup.find_all("a", href=True)
    links = soup.find("div", class_='imgTagWrapper')
    # links = soup.find_all('img')
    try:
        for link in links.find_all('img', alt=True):
            # link = link['src']
            title = link['alt']
            print(title)
            # image_bytes = requests.get(link, cookies=cookies, headers=headers).content  #работает
            # with open('amazom_B07B94ZR74.jpg', 'wb') as file:
            #     file.write(image_bytes)
    except Exception as ex:
        print(ex)
            
        

if __name__ == '__main__':
   
    # get_source_json()
    get_result()

