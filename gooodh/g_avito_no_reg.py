import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_avito_user(url):
    #использование юзер установленного хрома(работает при запуске одной копии хрома)
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--user-data-dir=c:\\Users\\Ser\\AppData\\Local\\Google\\Chrome\\User Data")

    s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    get_avito(url, driver)


def get_avito(url, driver):
    driver.get(url=url)
    time.sleep(10)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[3]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span/div/div/button').click()
    time.sleep(5)
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
    time.sleep(5)
    driver.quit()

def soup_phone():
    with open('page.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    soup_phon = soup.find('img', class_='button-phone-image-LkzoU button-phone-image_header-WDrLw').text
    with open('phone.txt', 'w') as file:
        file.write(soup_phon)

if __name__ == '__main__':
    # url = 'https://www.avito.ru/barnaul/doma_dachi_kottedzhi/dom_122m_na_uchastke_107sot._2711128614'
    soup_phone()
    # get_avito_user(url)
