import json


import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://cars.av.by/',
    'x-device-type': 'web.desktop',
    'Content-Type': 'application/json',
    'Origin': 'https://cars.av.by',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'page': 2,
    'properties': [
        {
            'name': 'price_currency',
            'value': 2,
        },
    ],
    'sorting': 1,
}

response = requests.post('https://api.av.by/offer-types/cars/filters/main/apply', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"page":2,"properties":[{"name":"price_currency","value":2}],"sorting":1}'
#response = requests.post('https://api.av.by/offer-types/cars/filters/main/apply', headers=headers, data=data)

print(response.status_code)

with open(f'avto.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False)



