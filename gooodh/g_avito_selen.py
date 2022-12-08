from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json
from selenium.webdriver.common.by import By


def get_source_html(url):
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(ua.random)
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(10)
        button = driver.find_element(By.CLASS_NAME, 'desktop-1kdcmzd')
        time.sleep(50)
        button.click()

        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def get_result():
    with open('page.html', 'r', encoding='utf-8') as file:
        products_data = file.read()
    soup = BeautifulSoup(products_data, 'lxml')
    soup_headers = soup.find_all('h3', class_='title-root-zZCwT body-title-drnL0 title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO')
    soup_prices = soup.find_all('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')


    filtere_price=[]

    for price in soup_prices:
        print(price.text)
        # filtere_price.append(str(price.text))
        # print(filtere_price)

    # filtere_headers=[]

    # for header in soup_headers:
    #     filtere_price.append(header.text)
    #     print(filtere_headers)



# <h3 itemprop="name" class="title-root-zZCwT body-title-drnL0 title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO">4-к. квартира, 76&nbsp;м², 4/5&nbsp;эт.</h3>
#<span class="price-text-_YGDY text-text-LurtD text-size-s-BxGpL">6&nbsp;500&nbsp;000<!-- -->&nbsp;<span class="price-currency-_FNLV">₽</span></span>
if __name__ == '__main__':
    # url = 'https://www.avito.ru/barnaul/nedvizhimost'
    # get_source_html(url)
    get_result()
