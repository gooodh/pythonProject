from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.avito.ru/')

with open(f'index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
