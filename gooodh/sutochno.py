import requests
import json


cookies = {
    'x-request-id': '35062bd6c918c02e49774d43c6041f62',
    'rid': '35062bd6c918c02e49774d43c6041f62',
    'route': '1677478825.052.60.51232|cb1faa23db9e30603aef3c84465716e1',
    'PHPSESSID': '6f50a9476d7e6fbf3350ead4d02e6bab',
    'language_id': 'ru',
    'x-request-id': '8368baedf0aa6f4d0875202c46947488',
    'rid': '8368baedf0aa6f4d0875202c46947488',
    'select_guests': '%7B%22guests%22%3A%7B%22adults%22%3A2%2C%22childrens%22%3A%5B%5D%7D%7D',
    '_me_': 'fB36QnKDuLeFMyeSN3Gwgg',
    '_gcl_au': '1.1.637749176.1677478825',
    '_ga_QFVTBCKP86': 'GS1.1.1677478825.1.1.1677481655.50.0.0',
    '_ga': 'GA1.2.2128120006.1677478826',
    '_gid': 'GA1.2.1351776290.1677478827',
    '_ym_uid': '1677478827247410997',
    '_ym_d': '1677478827',
    'tmr_lvid': 'd441844c2b07aeb620a8dc3d2fb1149c',
    'tmr_lvidTS': '1677478827796',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1677481075165',
    'calendar_dates': '%7B%22date_begin%22%3A%222023-02-28%22%2C%22date_end%22%3A%222023-03-01%22%7D',
    '_ym_visorc': 'b',
    '_gat_gtag_UA_2178778_2': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'api-version': 'null',
    'platform': 'js',
    'token': 'Hy6U3z61fflbgT2yJ/VdlQ2719',
    'Alt-Used': 'sutochno.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://sutochno.ru/front/searchapp/search?guests_adults=2&occupied=2023-02-28;2023-03-01&id=287390&type=city&term=%D0%A1%D0%BE%D1%87%D0%B8&SW.lat=42.56812434947174&SW.lng=38.61588889160158&NE.lat=44.72576680062264&NE.lng=41.14823752441409',
    # 'Cookie': 'x-request-id=35062bd6c918c02e49774d43c6041f62; rid=35062bd6c918c02e49774d43c6041f62; route=1677478825.052.60.51232|cb1faa23db9e30603aef3c84465716e1; PHPSESSID=6f50a9476d7e6fbf3350ead4d02e6bab; language_id=ru; x-request-id=8368baedf0aa6f4d0875202c46947488; rid=8368baedf0aa6f4d0875202c46947488; select_guests=%7B%22guests%22%3A%7B%22adults%22%3A2%2C%22childrens%22%3A%5B%5D%7D%7D; _me_=fB36QnKDuLeFMyeSN3Gwgg; _gcl_au=1.1.637749176.1677478825; _ga_QFVTBCKP86=GS1.1.1677478825.1.1.1677481655.50.0.0; _ga=GA1.2.2128120006.1677478826; _gid=GA1.2.1351776290.1677478827; _ym_uid=1677478827247410997; _ym_d=1677478827; tmr_lvid=d441844c2b07aeb620a8dc3d2fb1149c; tmr_lvidTS=1677478827796; _ym_isad=2; tmr_detect=0%7C1677481075165; calendar_dates=%7B%22date_begin%22%3A%222023-02-28%22%2C%22date_end%22%3A%222023-03-01%22%7D; _ym_visorc=b; _gat_gtag_UA_2178778_2=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def get_source_json():
    response = requests.get(
        'https://sutochno.ru/api/json/search/searchObjects?guests_childrens=&max_guests=2&occupied=2023-02-28%3B2023-03-01&currency_id=1&NE[lat]=44.72576680062264&NE[lng]=41.14823752441409&SW[lat]=42.56812434947174&SW[lng]=38.61588889160158&zoom=13&count=50&offset=200',
        cookies=cookies,
        headers=headers,
    )


    with open(f'sutochno.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False)

def get_result():

    with open('avito.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)


    with open(f'avito{cur_time}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                'id',
                'Название',
                'Локация',
                'Цена',
                'Примечание',
                'Дата, время публикации',
                'Url'
            ]
        )

   
        
    for item in json_data['items']:

        category = item['category']['slug']
        if category in 'kvartiry':
            
            title = item['title'].replace('&nbsp;', ' ')
            timestamp = datetime.fromtimestamp(item['sortTimeStamp'])
            timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H %M')
            url_off = 'https://www.avito.ru' + item['urlPath'].strip()

            with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
                writer = csv.writer(file)

                writer.writerow(
                    [
                        item['id'],
                        title,
                        item['location']['name'],
                        item['priceDetailed']['value'],
                        item['priceDetailed']['postfix'],
                        timestamp,
                        url_off
                    ]
                )

if __name__ == '__main__':
   
    # get_source_json()
    get_result()