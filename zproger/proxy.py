import requests


def handler():
    link = 'https://icanhazip.com/'
    proxies = {
        # 'http': f'http://190.61.88.147:8080',
        'https': f'http://40.129.203.4:8080'
    }
    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP:{response.strip()}')
    except:
        print('ex')

if __name__ == '__main__':
    handler()