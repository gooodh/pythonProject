from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
import datetime
from bs4 import BeautifulSoup

ua = UserAgent()  #
options = webdriver.ChromeOptions()
options.add_argument(ua.random)
options.add_argument("--disable-blink-features=AutomationControlled")

# linux
# driver = webdriver.Chrome(
#     executable_path="/path/chromedriver",
#     options=options
# )
# Указываем полный путь к geckodriver.exe на вашем ПК.
# s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=options)

cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
ua = UserAgent()  # пример Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': ua.random
}

try:
    response = requests.get(url='https://www.zarseti.ru/Home', headers=headers)

    with open(f'index.html', 'w') as file:
        file.write(response.text)

    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")

    # time.sleep(10)
except Exception as ex:
    print(ex)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
data_g = soup.find('div', class_='Blackouts').text.strip()
print(data_g)
# finally:
#     driver.close()
#     driver.quit()
