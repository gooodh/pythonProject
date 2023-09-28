
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
    '_ga_M29JC28873': 'GS1.1.1677325443.21.1.1677325564.7.0.0',
    '_ga': 'GA1.1.1310449360.1675056963',
    '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
    '__zzatw-avito': 'MDA0dBA=Fz2+aQ==',
    'tmr_lvid': 'b4e724a2edc2843a6c5c08c6a56618be',
    'tmr_lvidTS': '1675056965287',
    'cto_bundle': '-04uaV9aZW1CUTJDZ1JFVFVocEdyaHk5Yk8lMkZ0UDUlMkZGc2w5JTJCJTJGVmxaRDBNNXB0R2FFZDVvY2x5a2tHSW5tZm80M2pxUTIwdyUyQlU1RlZnb0xNSTdhbWhLZ0NKeURDYW5DaG5vY3hwSENGWWVBTFg2OWFLR2gzWmJNVHBiVFhQWXpSTVk0T1k',
    'cfidsw-avito': 'E+mtGS2rkrN6i0aeS8d6/uR7an58kdOvs/IjpkIkMhraLAKoxSQVnEXphsIat3JsBBc87Mk/WzphOcSCQXH3Wem+csB9Ux4npDgOXq03QW8WRFzp7uCWv7DtK3lVQIskdE9XyLF+qpcgvex+MhjSdAxpuPTzZyjDExu3',
    'adrcid': 'AEq7KH5wx6yp0Vz6p4nl_1w',
    'cfidsw-avito': 'NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N',
    'cfidsw-avito': 'NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N',
    'gsscw-avito': '+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==',
    'gsscw-avito': '+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==',
    'fgsscw-avito': 'XlLX3c3caadbbe365d310701bc531bfcd744f819',
    'fgsscw-avito': 'XlLX3c3caadbbe365d310701bc531bfcd744f819',
    '_buzz_fpc': 'JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyU3VuJTJDJTIwMjUlMjBGZWIlMjAyMDI0JTIwMTElM0E0NiUzQTA3JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyMzFmZTRiNDc1MmRhZTI1ZmM5NTBmNDUyMjE5OWJlZTUlNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==',
    'sessid': '3b7989d05f24cf807aea2bb609188701.1675057021',
    'auth': '1',
    'uxs_uid': '41add7d0-a060-11ed-b5db-832417414495',
    'sx': 'H4sIAAAAAAAC%2F1TQSXKsMAwA0Lt43QtZtmSpb4MnEoaCdqADSXH3X3%2BRVPoCb%2FG%2BjYegAUoEIGQhyZxiVMulw5BDF8392zzN3fTHpDat0mQf5nP7eHA700z%2BYzobn%2B%2FmZoq5Ww7BW6tI180E9hjBdT6LIIBiSNGnUoUqA2b6kZfG%2FRDOvQ8x%2B2Ndj3527ElnN4zI56ts4boZYUfOueicLRko%2Bdo5G4Q15eAs5h85vh2h4MPbtrea9tpqWrD3W3y6UXr%2FRwYl%2BC9rUlu4YobOphJ9FwQScvRJBUV%2F5WmoRxrHZ22KgR7RLW1426QudZas66uMet1MDa5mijlX8OC9oEOgSqWA2qzpd4P42D7tJ20rxWlnOdbcvXfbBOtX3cav1w3S6%2FoXAAD%2F%2F58jR1HDAQAA',
    'buyer_popup_location': '637640',
    'SEARCH_HISTORY_IDS': '4%2C1',
    'abp': '0',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1677325568715',
    'f': '5.df155a60305e515a2d6059f4e9572c01630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6357212485bdbc727357212485bdbc727357212485bdbc72738b4a54cef5443c1d8b16176e03d287314e2ef927eb99aa946b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8baed66fa7192f00c615ab5228c34303140e3fb81381f3591956cdff3d4067aa559b49948619279110df103df0c26013a1d6703cbe432bc2af722fe85c94f7d0c2da10fb74cac1eabdc5322845a0cba1af722fe85c94f7d0c2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd853206102760b3e6de87ad3b397f946b4c41e97fe93686addf6c43f31524d8e2264dccdfe25188ff5d3d12014bda85a4e203e99ef1367c11a0f2581016d7a8309154f4aaf0a7b4f411173486682b627f136195b2007053952ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd74829b0f7d7947a44063de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03',
    'ft': '"WQpLqnfxIlLrVYLcDyHYphhqUTrL+zDgXI2WyTjewW5uHXgDq0puW7PxGh+44D69DyF5ruG25UE/mhVtBzETVscagDlXpGWg0muu/XJHHFh8A228Cy8GPd6L+TCmOuOZnsLkKdJiDgFIsMBDDxV/A0urVuCaYVYDP2wanqBSEl+3mXicVkEsMD6jcZv0S8l0"',
    'luri': 'moskva',
    'v': '1677325443',
    '_ym_visorc': 'b',
    'isLegalPerson': '0',
    'dfp_group': '84',
    'buyer_from_page': 'catalog',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.avito.ru/moskva/noutbuki/dell-ASgCAQICAUCo5A0U1Nlm?cd=1',
    # 'Cookie': 'u=2xpxhprl.lskmu8.1jp3kkkzmwt00; buyer_laas_location=637640; buyer_location_id=637640; _ym_uid=1675056961769140913; _ym_d=1675056961; _gcl_au=1.1.1023169821.1675056962; _ga_M29JC28873=GS1.1.1677325443.21.1.1677325564.7.0.0; _ga=GA1.1.1310449360.1675056963; __zzatw-avito=MDA0dBA=Fz2+aQ==; __zzatw-avito=MDA0dBA=Fz2+aQ==; tmr_lvid=b4e724a2edc2843a6c5c08c6a56618be; tmr_lvidTS=1675056965287; cto_bundle=-04uaV9aZW1CUTJDZ1JFVFVocEdyaHk5Yk8lMkZ0UDUlMkZGc2w5JTJCJTJGVmxaRDBNNXB0R2FFZDVvY2x5a2tHSW5tZm80M2pxUTIwdyUyQlU1RlZnb0xNSTdhbWhLZ0NKeURDYW5DaG5vY3hwSENGWWVBTFg2OWFLR2gzWmJNVHBiVFhQWXpSTVk0T1k; cfidsw-avito=E+mtGS2rkrN6i0aeS8d6/uR7an58kdOvs/IjpkIkMhraLAKoxSQVnEXphsIat3JsBBc87Mk/WzphOcSCQXH3Wem+csB9Ux4npDgOXq03QW8WRFzp7uCWv7DtK3lVQIskdE9XyLF+qpcgvex+MhjSdAxpuPTzZyjDExu3; adrcid=AEq7KH5wx6yp0Vz6p4nl_1w; cfidsw-avito=NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N; cfidsw-avito=NKDA0Q4VEMecD5ZKYEEVzW+q5vx0EQT8ZB+2u9uLD1EcduYhOzJzNj//cmKelkLewqgzqfd4JdFhPbatk6zCJYXH7u5hcT6ny5lmU0O4AiSqPhPF6zUAX5697dguUateE6INjfBRlIwmuda+omAMvvMuDxHrPAMtr10N; gsscw-avito=+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==; gsscw-avito=+07/tglWlLBV57m8dNoerANK6B/vWmn2mqQIIT3EYA969Dic5GZD2v4tmuv7gI/LJ7OwQueeDXj6KYKhKVROFN4JvNbrf/iOTDPP6wwxm8uPpshKvCVqrIJVR4BKBFLYH1ENNBwjB//WZiWWih4aprsyKnKuH8k5NttEgjnJM9yzBGEnm330/g03yHMj2YI56oTFKKA1CzZNZALfkyXTXO3eZUvzuyqSAQkKSsXdeFMY6UysnpEoEg8iw7T0BKmaZA==; fgsscw-avito=XlLX3c3caadbbe365d310701bc531bfcd744f819; fgsscw-avito=XlLX3c3caadbbe365d310701bc531bfcd744f819; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyU3VuJTJDJTIwMjUlMjBGZWIlMjAyMDI0JTIwMTElM0E0NiUzQTA3JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyMzFmZTRiNDc1MmRhZTI1ZmM5NTBmNDUyMjE5OWJlZTUlNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; sessid=3b7989d05f24cf807aea2bb609188701.1675057021; auth=1; uxs_uid=41add7d0-a060-11ed-b5db-832417414495; sx=H4sIAAAAAAAC%2F1TQSXKsMAwA0Lt43QtZtmSpb4MnEoaCdqADSXH3X3%2BRVPoCb%2FG%2BjYegAUoEIGQhyZxiVMulw5BDF8392zzN3fTHpDat0mQf5nP7eHA700z%2BYzobn%2B%2FmZoq5Ww7BW6tI180E9hjBdT6LIIBiSNGnUoUqA2b6kZfG%2FRDOvQ8x%2B2Ndj3527ElnN4zI56ts4boZYUfOueicLRko%2Bdo5G4Q15eAs5h85vh2h4MPbtrea9tpqWrD3W3y6UXr%2FRwYl%2BC9rUlu4YobOphJ9FwQScvRJBUV%2F5WmoRxrHZ22KgR7RLW1426QudZas66uMet1MDa5mijlX8OC9oEOgSqWA2qzpd4P42D7tJ20rxWlnOdbcvXfbBOtX3cav1w3S6%2FoXAAD%2F%2F58jR1HDAQAA; buyer_popup_location=637640; SEARCH_HISTORY_IDS=4%2C1; abp=0; _ym_isad=2; tmr_detect=0%7C1677325568715; f=5.df155a60305e515a2d6059f4e9572c01630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6357212485bdbc727357212485bdbc727357212485bdbc72738b4a54cef5443c1d8b16176e03d287314e2ef927eb99aa946b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8baed66fa7192f00c615ab5228c34303140e3fb81381f3591956cdff3d4067aa559b49948619279110df103df0c26013a1d6703cbe432bc2af722fe85c94f7d0c2da10fb74cac1eabdc5322845a0cba1af722fe85c94f7d0c2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd853206102760b3e6de87ad3b397f946b4c41e97fe93686addf6c43f31524d8e2264dccdfe25188ff5d3d12014bda85a4e203e99ef1367c11a0f2581016d7a8309154f4aaf0a7b4f411173486682b627f136195b2007053952ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd74829b0f7d7947a44063de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03; ft="WQpLqnfxIlLrVYLcDyHYphhqUTrL+zDgXI2WyTjewW5uHXgDq0puW7PxGh+44D69DyF5ruG25UE/mhVtBzETVscagDlXpGWg0muu/XJHHFh8A228Cy8GPd6L+TCmOuOZnsLkKdJiDgFIsMBDDxV/A0urVuCaYVYDP2wanqBSEl+3mXicVkEsMD6jcZv0S8l0"; luri=moskva; v=1677325443; _ym_visorc=b; isLegalPerson=0; dfp_group=84; buyer_from_page=catalog',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'cd': '1',
    # 'p': '2',
}



def get_source_html():
    response = requests.get(
    'https://www.avito.ru/moskva/noutbuki/dell-ASgCAQICAUCo5A0U1Nlm',
    params=params,
    cookies=cookies,
    headers=headers,
)
    with open('avito.html', 'w', encoding='utf-8') as file:
        file.write(response.text)


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
        if 'Intel i7' in title:
            link_l.append(link)
            title_l.append(title)

    rows = zip(title_l, price_l, description_l, link_l)
        
    with open(f'avito{cur_time}.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':
   
    # get_source_html()
    get_result()

