import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



    
def get_source_html(url):
    driver = webdriver.Firefox(executable_path='/home/nikulin/geckodriver')
    #driver = webdriver.Chrome(executable_path='/home/nikulin/chromedriver')
    try:
        driver.get(url=url)
        time.sleep(10)
        
        with open('ya.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)
    
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def get_result():
    with open('ya.html', 'r', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')#_3wtYw _2OAAC undefined cia-cs
    title = soup.find('a', class_='_2f75n JqCMK cia-cs').text
    description = soup.find('div', class_='_2J3K5').text
    specifications = soup.find('div', class_='cia-vs cia-cs').text
    print(specifications)

if __name__ == '__main__':
   
    # url='https://market.yandex.ru/product--fotoapparat-canon-eos-450d-kit/1592825/spec?clid=2357258&distr_type=7&utm_source=admitad&utm_medium=cpa&utm_campaign=843361&utm_term=https%3A%2F%2Fymarket-tops.ru%2F&pp=900&vid=e3e354039a48000d667bfca07662c014&mclid=1003&cpa=1'

    # get_source_html(url)
    get_result()