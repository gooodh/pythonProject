from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

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


if __name__ == '__main__':
    url = 'https://www.avito.ru/barnaul/nedvizhimost'
    get_source_html(url)
