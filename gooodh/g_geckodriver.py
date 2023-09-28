import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Firefox(executable_path='/home/nikulin/geckodriver')
#driver = webdriver.Chrome(executable_path='/home/nikulin/chromedriver')
# driver.get('https://www.google.com/')
url='https://www.zara.com/tr/tr/session/login'
# response = requests.post('https://www.zara.com/tr/tr/session/login', params=params,
try:
    driver.get(url=url)
    time.sleep(10)
    with open('zara.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

    # all_title = driver.find_element(By.CLASS_NAME,"title")
    # title = [title.text for title in all_title]
    # print(title)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

# page_url = driver.find_elements_by_xpath("//a[@class='content']")
# all_title = driver.find_elements_by_class_name("title")
# title = [title.text for title in all_title]
# print(title)

# geckodriver_autoinstaller.install()

# profile = webdriver.FirefoxProfile(
#     # '/Users/<user name>/Library/Application Support/Firefox/Profiles/xxxxx.default-release')
#     'c:\\Users\\Ser\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\nyc96wln.default-release')
#
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()
# desired = DesiredCapabilities.FIREFOX
#
# driver = webdriver.Firefox(firefox_profile=profile,
#                            desired_capabilities=desired)
