import requests


def handler(proxy):
    link = 'https://icanhazip.com/'
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP:{response.strip()}')
    except:
        print('ex')