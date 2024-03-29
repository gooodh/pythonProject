import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

PROXY_HOST = '89.208.219.121'
PROXY_PORT = 8080  # Your proxy port
PROXY_USER = 'PROXY_USER'
PROXY_PASS = 'PROXY_PASS'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"76.0.0"
}
"""

background_js = """
let config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}
chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)

        chrome_options.add_extension(plugin_file)

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')
    s = Service(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

    # s = Service(
    #     executable_path='path_to_chromedriver'
    # )
    driver = webdriver.Chrome(
        service=s,
        options=chrome_options
    )

    return driver


def main():
    driver = get_chromedriver(use_proxy=True,
                              user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15')
    # driver.get('https://2ip.ru')
    driver.get('https://2gis.ru/barnaul/search/Авто')
    # driver.get('https://bot.sannysoft.com/')

    # driver.get('https://whatmyuseragent.com/')
    # driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')# сайт проверка бот или нет
    sleep(10)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()