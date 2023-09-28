# import undetected_chromedriver as uc
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import time
from datetime import datetime
import json
import csv

# from selenium_stealth import stealth

cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')
def get_avito_user(url):
    #использование юзер установленного хрома(работает при запуске одной копии хрома)
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    # e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
    # options.add_argument("--user-data-dir=c:\\Users\\Ser\\AppData\\Local\\Google\\Chrome\\User Data")
    # driver = uc.Chrome(options=options)
    # s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    # driver = webdriver.Chrome(service=s, options=options)
    options.add_argument("--user-data-dir=/home/nikulin/.mozilla/firefox/9sf8n1nd.default")
    driver = webdriver.Firefox(executable_path='/home/nikulin/geckodriver')
    driver.get(url=url)
    #get_avito(url, driver)

def get_source_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument(
        argument='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36')
    options.add_argument("--disable-blink-features=AutomationControlled")

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    s = Service(executable_path='/home/nikulin/geckodriver')
    driver = webdriver.Firefox(service=s, options=options)
    driver.maximize_window()
    # get_avito(url, driver)

def get_avito(url,driver):
    #регистрация
    driver.get(url=url)
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/div[2]/a').click()
    time.sleep(5)
    driver.find_element(By.NAME, 'login').send_keys('+79236558669')
    time.sleep(2)
    driver.find_element(By.NAME, 'password').send_keys('qWX8vP_V')
    time.sleep(2)
    driver.find_element(By.NAME, 'submit').click()
    time.sleep(20)
    # driver.get('https://www.avito.ru/barnaul/doma_dachi_kottedzhi/dom_122m_na_uchastke_107sot._2711128614')
    time.sleep(30)

    driver.quit()


# def get_source_stealth(url):
#     #использование стелс
#     options = webdriver.ChromeOptions()
#     options.add_argument("start-maximized")
#
#     # options.add_argument("--headless")
#
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
#     driver = webdriver.Chrome(service=s, options=options)
#
#     stealth(driver,
#             languages=["ru-RU", "ru"],
#             vendor="Google Inc.",
#             platform="Win32",
#             webgl_vendor="Intel Inc.",
#             renderer="Intel Iris OpenGL Engine",
#             fix_hairline=True,
#             )
#
#     get_avito(url,driver)


if __name__ == '__main__':
    url = 'https://www.ozon.ru/'
    # url = 'https://www.avito.ru/#login?authsrc=h'
    # url = 'https://bot.sannysoft.com/'
    # get_source_html(url)
    # get_source_stealth(url)
    get_avito_user(url)
