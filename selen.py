from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ua = UserAgent()#
options = webdriver.ChromeOptions()
options.add_argument(ua.random)
options.add_argument("--disable-blink-features=AutomationControlled")

# linux
# driver = webdriver.Chrome(
#     executable_path="/path/chromedriver",
#     options=options
# )
# Указываем полный путь к geckodriver.exe на вашем ПК.
s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
#
try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")

    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
