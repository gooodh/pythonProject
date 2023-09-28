import requests
import json

import requests

cookies = {
    'qrator_ssid': '1677586077.949.bO61GwgrHwGYsojE-9jull2akb26g67fucec6gnd0pbbfk49u',
    'qrator_jsid': '1677586077.399.93VMfZZw3Pq7AzFq-3imj2diuqg4cqvepuh3pk1424ei4j5af',
    'disp_react_aa': '2',
    'ggr-widget-test': '1',
    '_regionID': '2397',
    'cookie_accepted': 'true',
    'GACookieStorage': 'GA1.2.322188536.1677586085',
    '_ym_uid': '1677586084483724344',
    '_ym_d': '1677586084',
    '_ga_Z72HLV7H6T': 'GS1.1.1677586084.1.1.1677587807.0.0.0',
    '_ga': 'GA1.2.322188536.1677586085',
    'iap.uid': 'f1322769ca3b49058209a805fca90c64',
    '_ym_isad': '2',
    'tmr_lvid': '62f5e2985d5db18c16c0bb65b5fe159d',
    'tmr_lvidTS': '1677586085914',
    '_singleCheckout': 'true',
    '_unifiedCheckout': 'true',
    '_pickupMapSearch': 'true',
    'adrdel': '1',
    'adrcid': 'AAT5Eva9yh44ar-fYvIRd8w',
    'uxs_uid': '900789f0-b760-11ed-af06-19f864d9e985',
    '_gid': 'GA1.2.1217541199.1677586089',
    'sawOPH': 'true',
    'X-API-Experiments-sub': 'B',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json;charset=utf-8',
    'x-request-id': '8e962a5dfd76024c2a2cf7ca3c3850e9',
    'x-api-key': 'nkGKLkscp80GVAQVY8YvajPjzaFTmIS8',
    'Origin': 'https://barnaul.leroymerlin.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://barnaul.leroymerlin.ru/',
    # 'Cookie': 'qrator_ssid=1677586077.949.bO61GwgrHwGYsojE-9jull2akb26g67fucec6gnd0pbbfk49u; qrator_jsid=1677586077.399.93VMfZZw3Pq7AzFq-3imj2diuqg4cqvepuh3pk1424ei4j5af; disp_react_aa=2; ggr-widget-test=1; _regionID=2397; cookie_accepted=true; GACookieStorage=GA1.2.322188536.1677586085; _ym_uid=1677586084483724344; _ym_d=1677586084; _ga_Z72HLV7H6T=GS1.1.1677586084.1.1.1677587807.0.0.0; _ga=GA1.2.322188536.1677586085; iap.uid=f1322769ca3b49058209a805fca90c64; _ym_isad=2; tmr_lvid=62f5e2985d5db18c16c0bb65b5fe159d; tmr_lvidTS=1677586085914; _singleCheckout=true; _unifiedCheckout=true; _pickupMapSearch=true; adrdel=1; adrcid=AAT5Eva9yh44ar-fYvIRd8w; uxs_uid=900789f0-b760-11ed-af06-19f864d9e985; _gid=GA1.2.1217541199.1677586089; sawOPH=true; X-API-Experiments-sub=B',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

json_data = {
    'regionCode': 'barnaul',
    'productId': '82038773',
    'unit': 'шт.',
    'currencyKey': 'RUB',
    'preferedStores': [],
    'source': 'Step',
}



# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"regionCode":"barnaul","productId":"82038773","unit":"шт.","currencyKey":"RUB","preferedStores":[],"source":"Step"}'.encode()
#response = requests.post(
#    'https://api.leroymerlin.ru/experience/LeroymerlinWebsite/v1/navigation-pdp-api//get-stocks',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

def get_source_json():
    
    response = requests.post(
    'https://api.leroymerlin.ru/experience/LeroymerlinWebsite/v1/navigation-pdp-api//get-stocks',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
    with open(f'lerua.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False)


if __name__ == '__main__':
   
    get_source_json()
    # get_result()