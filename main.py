import schedule
import time as t
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('disable-notifications')

urls_list = ['https://yahoo.com/', 'https://eff.org/', 'https://invidious.io/']

def get_secondly_screenshots(list_of_urls):
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    for url in list_of_urls:
        driver.get(url)
        now = datetime.now()
        date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
        sh_url = url.split('://')[1].split('.')[0]
        print(sh_url, date_time)
        driver.save_screenshot(f'{sh_url}_{date_time}.png')

        print('screenshotted ', url)
        t.sleep(2)
    driver.quit()

schedule.every(10).seconds.do(get_secondly_screenshots, list_of_urls = urls_list)
while True:
    schedule.run_pending()
    t.sleep(1)