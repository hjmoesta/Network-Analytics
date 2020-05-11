import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def speed_test():
    home_dir = os.path.expanduser('~')
    webdriver_dir = os.path.join(home_dir, 'Downloads/chromedriver')
    driver = webdriver.Chrome(webdriver_dir)
    driver.get('http://speedtest.net')
    button = driver.find_element_by_class_name("js-start-test.test-mode-multi")
    button.click()

    time.sleep(60)

    download = driver.find_element_by_class_name("result-data-large.number.result-data-value.download-speed")
    upload = driver.find_element_by_class_name("result-data-large.number.result-data-value.upload-speed")
    download_speed = download.get_attribute('innerHTML')
    upload_speed = upload.get_attribute('innerHTML')
    driver.quit()
    print(upload_speed,download_speed)
speed_test()