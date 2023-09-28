
from bs4 import BeautifulSoup

import requests

import json
import csv
from datetime import datetime

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')

cookies = {
    'u': '2xpxhprl.lskmu8.1jp3kkkzmwt00',
    'buyer_laas_location': '637640',
    'buyer_location_id': '637640',
    '_ym_uid': '1675056961769140913',
    '_ym_d': '1675056961',
    '_gcl_au': '1.1.1023169821.1675056962',
    '_ga_M29JC28873': 'GS1.1.1676980279.13.1.1676983339.55.0.0',
    '_ga': 'GA1.1.1310449360.1675056963',
    '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
    '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
    'tmr_lvid': 'b4e724a2edc2843a6c5c08c6a56618be',
    'tmr_lvidTS': '1675056965287',
    'cto_bundle': 'U6vSb19PMlFuN0pkd1pqRDFPR2thTFpiakhuVXhraXFSR3d1JTJGVlR5OTNNdkYlMkJjd2lsaUNMaTQzMXVFOTNnMW9tS3pmeVlxJTJGR3VxQjVwbTNEOFd5cFBCZXFrejZxZEhrU0gySVRtb3VUelc4NmR6NjI4OGg0aVNVU3p3ZUFlSnZWVUgzeQ',
    'cfidsw-avito': 'E+mtGS2rkrN6i0aeS8d6/uR7an58kdOvs/IjpkIkMhraLAKoxSQVnEXphsIat3JsBBc87Mk/WzphOcSCQXH3Wem+csB9Ux4npDgOXq03QW8WRFzp7uCWv7DtK3lVQIskdE9XyLF+qpcgvex+MhjSdAxpuPTzZyjDExu3',
    'adrcid': 'AEq7KH5wx6yp0Vz6p4nl_1w',
    'cfidsw-avito': 'NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N',
    'cfidsw-avito': 'NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N',
    'gsscw-avito': '+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==',
    'gsscw-avito': '+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==',
    'fgsscw-avito': 'XlLX3c3caadbbe365d310701bc531bfcd744f819',
    'fgsscw-avito': 'XlLX3c3caadbbe365d310701bc531bfcd744f819',
    '_buzz_fpc': 'JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyV2VkJTJDJTIwMjElMjBGZWIlMjAyMDI0JTIwMTIlM0E0MiUzQTI0JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyMzFmZTRiNDc1MmRhZTI1ZmM5NTBmNDUyMjE5OWJlZTUlNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==',
    'sessid': '3b7989d05f24cf807aea2bb609188701.1675057021',
    'auth': '1',
    'uxs_uid': '41add7d0-a060-11ed-b5db-832417414495',
    'sx': 'H4sIAAAAAAAC%2F1TSSY7qQAzG8btkzaLKdnno29QIhDRJIAzhibs%2FsQA1F%2FjJ%2Bvv71zkzMM%2FeKbOXmAOrUYolGkQPoXU%2F%2F7pr99MZ58tsdMdht5sQlvpwt9NNXFwe41Zdt%2Blq9%2BNZxLEJ4nPTQRUhCCql1QBgKVrl0JjRkY8V3zLgYsuhkSLew9mFdV6naZaByoA3Pv%2BVxYI9N11IqXHQQiFFc1nZiuUWGmkBRym%2B5cICB7HFoBfo3eWYaiU%2BXW7ndj7R9CWjvm6WYtIQMkUmFeIYa0Qjy2w5OM1vWa3RcGynS8ZpKOu6j1s%2Ft9thlTbMl2%2FZq39uutSUuBKHlH0mZG5KQGRWiwWDT%2BfW%2B2k899brPA0ztF6cW93h2ovUkh9fMjt9brpsFKSyVEfREimgVfMAKuik8qczthEtxulsEK%2F%2BPhYuMZno9b7iPi1fcsDwkmsJ3HwW1Fg0mAWnTok5kJAlecsnuO7326FK1m2IMA1D%2Bo12cAr347LNf%2BUX%2Fdx0JbSkThqXFg3RslTNiWryGRwBfT74uMJ%2BQtrhiP3BrfPIv%2Bim7XGcYtDwJTO%2FatRcS80VTdinBMmbV%2BdKqFU4AtXPno%2FDwnse8XJPjq%2FhAOuCJ7Hd766e1%2B%2FVBbbn838AAAD%2F%2FzwtVxkrAwAA',
    'abp': '0',
    'buyer_popup_location': '637640',
    'luri': 'moskva',
    'SEARCH_HISTORY_IDS': '1',
    'f': '5.df155a60305e515a2d6059f4e9572c01630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6357212485bdbc727357212485bdbc727357212485bdbc72738b4a54cef5443c1d8b16176e03d287314e2ef927eb99aa946b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8baed66fa7192f00c615ab5228c34303140e3fb81381f3591956cdff3d4067aa559b49948619279110df103df0c26013a1d6703cbe432bc2af722fe85c94f7d0c2da10fb74cac1eabdc5322845a0cba1af722fe85c94f7d0c2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd853206102760b3e6de87ad3b397f946b4c41e97fe93686addf6c43f31524d8e2264dccdfe25188ff5d3d12014bda85a4e203e99ef1367c11a0f2581016d7a8309154f4aaf0a7b4f411173486682b627f136195b2007053952ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748fa567cf1a09764a93de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03',
    'ft': '"IRIVlLpQzFV/v/XCiMg7bRCXrx2B1LSrl+Jg1e42a4R53laU8e5vyXtcbCKxzQ08Jl8S7YdRhajSyJKGs2OG7DD0HnguIibVw0C/NxIQyiKCEJhDuihGjaorexii9TLuD2mzHZ7ECwiwggAow2gWDXJIBRvwMxO/OeDP4B3XpOLOzrXG/YWMk9HM9bIOAD8+"',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'tmr_detect': '0%7C1676983346828',
    'v': '1676980781',
    'dfp_group': '24',
    'isLegalPerson': '0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.avito.ru/moskva/nedvizhimost?cd=1',
    'content-type': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'x-source': 'client-browser',
    'Connection': 'keep-alive',
    # 'Cookie': 'u=2xpxhprl.lskmu8.1jp3kkkzmwt00; buyer_laas_location=637640; buyer_location_id=637640; _ym_uid=1675056961769140913; _ym_d=1675056961; _gcl_au=1.1.1023169821.1675056962; _ga_M29JC28873=GS1.1.1676980279.13.1.1676983339.55.0.0; _ga=GA1.1.1310449360.1675056963; __zzatw-avito=MDA0dBA=Fz2+aQ==; __zzatw-avito=MDA0dBA=Fz2+aQ==; tmr_lvid=b4e724a2edc2843a6c5c08c6a56618be; tmr_lvidTS=1675056965287; cto_bundle=U6vSb19PMlFuN0pkd1pqRDFPR2thTFpiakhuVXhraXFSR3d1JTJGVlR5OTNNdkYlMkJjd2lsaUNMaTQzMXVFOTNnMW9tS3pmeVlxJTJGR3VxQjVwbTNEOFd5cFBCZXFrejZxZEhrU0gySVRtb3VUelc4NmR6NjI4OGg0aVNVU3p3ZUFlSnZWVUgzeQ; cfidsw-avito=E+mtGS2rkrN6i0aeS8d6/uR7an58kdOvs/IjpkIkMhraLAKoxSQVnEXphsIat3JsBBc87Mk/WzphOcSCQXH3Wem+csB9Ux4npDgOXq03QW8WRFzp7uCWv7DtK3lVQIskdE9XyLF+qpcgvex+MhjSdAxpuPTzZyjDExu3; adrcid=AEq7KH5wx6yp0Vz6p4nl_1w; cfidsw-avito=NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N; cfidsw-avito=NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N; gsscw-avito=+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==; gsscw-avito=+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==; fgsscw-avito=XlLX3c3caadbbe365d310701bc531bfcd744f819; fgsscw-avito=XlLX3c3caadbbe365d310701bc531bfcd744f819; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyV2VkJTJDJTIwMjElMjBGZWIlMjAyMDI0JTIwMTIlM0E0MiUzQTI0JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyMzFmZTRiNDc1MmRhZTI1ZmM5NTBmNDUyMjE5OWJlZTUlNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; sessid=3b7989d05f24cf807aea2bb609188701.1675057021; auth=1; uxs_uid=41add7d0-a060-11ed-b5db-832417414495; sx=H4sIAAAAAAAC%2F1TSSY7qQAzG8btkzaLKdnno29QIhDRJIAzhibs%2FsQA1F%2FjJ%2Bvv71zkzMM%2FeKbOXmAOrUYolGkQPoXU%2F%2F7pr99MZ58tsdMdht5sQlvpwt9NNXFwe41Zdt%2Blq9%2BNZxLEJ4nPTQRUhCCql1QBgKVrl0JjRkY8V3zLgYsuhkSLew9mFdV6naZaByoA3Pv%2BVxYI9N11IqXHQQiFFc1nZiuUWGmkBRym%2B5cICB7HFoBfo3eWYaiU%2BXW7ndj7R9CWjvm6WYtIQMkUmFeIYa0Qjy2w5OM1vWa3RcGynS8ZpKOu6j1s%2Ft9thlTbMl2%2FZq39uutSUuBKHlH0mZG5KQGRWiwWDT%2BfW%2B2k899brPA0ztF6cW93h2ovUkh9fMjt9brpsFKSyVEfREimgVfMAKuik8qczthEtxulsEK%2F%2BPhYuMZno9b7iPi1fcsDwkmsJ3HwW1Fg0mAWnTok5kJAlecsnuO7326FK1m2IMA1D%2Bo12cAr347LNf%2BUX%2Fdx0JbSkThqXFg3RslTNiWryGRwBfT74uMJ%2BQtrhiP3BrfPIv%2Bim7XGcYtDwJTO%2FatRcS80VTdinBMmbV%2BdKqFU4AtXPno%2FDwnse8XJPjq%2FhAOuCJ7Hd766e1%2B%2FVBbbn838AAAD%2F%2FzwtVxkrAwAA; abp=0; buyer_popup_location=637640; luri=moskva; SEARCH_HISTORY_IDS=1; f=5.df155a60305e515a2d6059f4e9572c01630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6357212485bdbc727357212485bdbc727357212485bdbc72738b4a54cef5443c1d8b16176e03d287314e2ef927eb99aa946b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8baed66fa7192f00c615ab5228c34303140e3fb81381f3591956cdff3d4067aa559b49948619279110df103df0c26013a1d6703cbe432bc2af722fe85c94f7d0c2da10fb74cac1eabdc5322845a0cba1af722fe85c94f7d0c2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd853206102760b3e6de87ad3b397f946b4c41e97fe93686addf6c43f31524d8e2264dccdfe25188ff5d3d12014bda85a4e203e99ef1367c11a0f2581016d7a8309154f4aaf0a7b4f411173486682b627f136195b2007053952ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748fa567cf1a09764a93de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03; ft="IRIVlLpQzFV/v/XCiMg7bRCXrx2B1LSrl+Jg1e42a4R53laU8e5vyXtcbCKxzQ08Jl8S7YdRhajSyJKGs2OG7DD0HnguIibVw0C/NxIQyiKCEJhDuihGjaorexii9TLuD2mzHZ7ECwiwggAow2gWDXJIBRvwMxO/OeDP4B3XpOLOzrXG/YWMk9HM9bIOAD8+"; _ym_isad=2; _ym_visorc=b; tmr_detect=0%7C1676983346828; v=1676980781; dfp_group=24; isLegalPerson=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'forceLocation': 'false',
    'locationId': '637640',
    'lastStamp': '1676983333',
    'limit': '300',
    'offset': '300',
    'categoryId': '4',
}
def get_source_json():
    response = requests.get('https://www.avito.ru/web/1/main/items', params=params, cookies=cookies, headers=headers)

    with open(f'avito.json', 'w', encoding='utf-8') as file:
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

