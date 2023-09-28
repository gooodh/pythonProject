import requests
import json

cookies = {
    'ins_starshopkz': 'a24j6-5372907182796e8998b6c7e3196b2e14',
    'first_current_location': '%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov',
    'first_referer': '',
    'referer': '',
    'current_location': '%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov',
    'cart': '%7B%22comment%22%3Anull%2C%22payment_title%22%3Anull%2C%22payment_description%22%3Anull%2C%22delivery_description%22%3Anull%2C%22delivery_price%22%3A0.0%2C%22number%22%3Anull%2C%22delivery_date%22%3Anull%2C%22delivery_from_hour%22%3Anull%2C%22delivery_to_hour%22%3Anull%2C%22delivery_title%22%3Anull%2C%22delivery_from_minutes%22%3Anull%2C%22delivery_to_minutes%22%3Anull%2C%22items_count%22%3A0%2C%22items_price%22%3A0.0%2C%22order_lines%22%3A%5B%5D%2C%22discounts%22%3A%5B%5D%2C%22total_price%22%3A0.0%7D',
    'visit': 't',
    'this_page': 'https%3A%2F%2Fstarshop.kz%2Fcollection%2Faksessuary-1497329190',
    'product_ids': '302586829',
    '_ga': 'GA1.2.1636356834.1688616345',
    '_gid': 'GA1.2.829998536.1688616345',
    '_gat': '1',
    '_dc_gtm_UA-37853801-1': '1',
    'tmr_lvid': '1e84a57654672f071c63c07446f3551b',
    'tmr_lvidTS': '1688616345439',
    '_ym_uid': '1688616346496981185',
    '_ym_d': '1688616346',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1688616349090',
    '_ym_visorc': 'w',
    'welcome': 'closed',
    'ins_order_version': '1688616387.3706536',
    'prev_page': 'https%3A%2F%2Fstarshop.kz%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://starshop.kz/collection/aksessuary-1497329190',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': 'ins_starshopkz=a24j6-5372907182796e8998b6c7e3196b2e14; first_current_location=%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov; first_referer=; referer=; current_location=%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov; cart=%7B%22comment%22%3Anull%2C%22payment_title%22%3Anull%2C%22payment_description%22%3Anull%2C%22delivery_description%22%3Anull%2C%22delivery_price%22%3A0.0%2C%22number%22%3Anull%2C%22delivery_date%22%3Anull%2C%22delivery_from_hour%22%3Anull%2C%22delivery_to_hour%22%3Anull%2C%22delivery_title%22%3Anull%2C%22delivery_from_minutes%22%3Anull%2C%22delivery_to_minutes%22%3Anull%2C%22items_count%22%3A0%2C%22items_price%22%3A0.0%2C%22order_lines%22%3A%5B%5D%2C%22discounts%22%3A%5B%5D%2C%22total_price%22%3A0.0%7D; visit=t; this_page=https%3A%2F%2Fstarshop.kz%2Fcollection%2Faksessuary-1497329190; product_ids=302586829; _ga=GA1.2.1636356834.1688616345; _gid=GA1.2.829998536.1688616345; _gat=1; _dc_gtm_UA-37853801-1=1; tmr_lvid=1e84a57654672f071c63c07446f3551b; tmr_lvidTS=1688616345439; _ym_uid=1688616346496981185; _ym_d=1688616346; _ym_isad=2; tmr_detect=0%7C1688616349090; _ym_visorc=w; welcome=closed; ins_order_version=1688616387.3706536; prev_page=https%3A%2F%2Fstarshop.kz%2Fproduct%2Fkrem-gel-gardex-classic-protiv-ukusov-komarov',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'If-Modified-Since': 'Thu, 06 Jul 2023 04:05:07 GMT',
    'If-None-Match': '8c3624252c0aafa7e1307b227a83b9e9',
}

response = requests.get('https://starshop.kz/products_by_id/302586829.json', cookies=cookies, headers=headers)

print(response.status_code)

# with open('starshop.txt', 'w', encoding='utf-8') as file:
#     # json.dump(response.json(), file, ensure_ascii=False)
#     file.write(response.text)

