from selenium import webdriver
# import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox('c:\\Users\\Ser\\PycharmProjects\\pythonProject\\geckodriver.exe')

driver.get("http://www.google.com")

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
