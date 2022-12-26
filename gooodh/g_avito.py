import json

import requests

# url = 'https://www.avito.ru/barnaul/nedvizhimost?cd=1'
url = 'https://www.avito.ru/web/1/main/items?forceLocation=false&locationId=621630&lastStamp=1671697322&limit=30&offset=27&categoryId=4'

cookies = {
    'u': '2tj7uqff.hbx1uv.hmkdezkwarg0',
    '_ym_uid': '1665989131720235499',
    '_ym_d': '1665989131',
    '_gcl_au': '1.1.456253853.1665989131',
    'isCriteoSetNew': 'true',
    'buyer_location_id': '621630',
    'buyer_popup_location': '621630',
    '_ga': 'GA1.1.1318981853.1665989135',
    'adrcid': 'AXlQoVadZ4EIpQlhnTsPsPw',
    'buyer_laas_location': '621630',
    '_ga_9E363E7BES': 'GS1.1.1668407996.3.1.1668408131.60.0.0',
    'v': '1670226717',
    'luri': 'barnaul',
    'sx': 'H4sIAAAAAAAC/wTAwQ3CMAwF0F3+mUMsk28529DYqOJUQBRIld37DpBkD+Pd6ZVXetqS6mG19G7haAd2NAzp/9/3XV7bXtexZo5Fc3PN+PD2eOKCRBNaUVERm/MMAAD//xRoyqlbAAAA',
    'dfp_group': '89',
    'abp': '0',
    '_ga_M29JC28873': 'GS1.1.1670226723.4.0.1670226723.60.0.0',
    'cto_bundle': 'FLwwY19YdUlHWGFlUWclMkZiU2pESnJ3ZmJNbDdZenNZTkFPZ3NsajhRWlVQNUZxV0FvczJpWE5DWTV4emZvZkFFZkN5TGU3YWxIU1VYWE8lMkZIWnZtWlhKeUVnVEdhZyUyQnQlMkJSM3EyREYwMjRNVW1TTUozS1RkZyUyQm9FRGJ5WXQ0ZHRidW5iMlRxcjFvc2xIWGhCdndLTDNsYXVJZmdnJTNEJTNE',
    'tmr_detect': '0|1670226729567',
    '_ym_visorc': 'b',
    '_ym_isad': '1',
    '_buzz_fpc': 'JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyVHVlJTJDJTIwMDUlMjBEZWMlMjAyMDIzJTIwMDclM0E1MiUzQTIyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyOTJhY2JmY2ViOTc5YjkyMzIyNWUxNDgwNjU5MzUwYTklNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==',
    'f': '5.df155a60305e515a2d6059f4e9572c01630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6630247e51b9c7ed6357212485bdbc727357212485bdbc727357212485bdbc72738b4a54cef5443c13afa3d284af961c234bd85fe5e85ba0346b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e9bcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac2da10fb74cac1eab268a7bf63aa148d2dc5322845a0cba1aba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f2da10fb74cac1eabf0c77052689da50d0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad784707749ff54e5f451dae31c335012c02c730c0109b9fbbc60ec9d2f66a8631c9fbdd7f5877c6d729aa4cecca288d6b40eee9b0b3836f39b6c9122eda0b0e570df103df0c26013a0df103df0c26013aafbc9dcfc006bed91f68c9323f3babacee9ba4a24aa4b68d3de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f',
    'ft': '"3uyIZTkktEFYPxrXjnqiE7bqtIoFjfwf6Csh0LnMYoCdyKymVOmK3L92O1hpiFzCGwxkVTMBSsSMRTO8T46fEmZuF8AUBaatfobjEDtdHrTPMLWgTXchfRlj47Snnpu0Hz4+Zz+WtGzrmTR0je7M3KMKrcR+nzru7JY6ZtYsuSPNTP2FdWCKY9NRat5ObqFn"',
    'buyer_from_page': 'main'}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'pragma': 'no-cache',
    'referer': 'https://www.avito.ru/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
s = requests.session()
response = s.get(url, cookies=cookies, headers=headers)

with open('data_res.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)