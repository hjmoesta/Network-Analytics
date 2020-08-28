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
    driver.get('http://speedtest.net/')
    button = driver.find_element_by_class_name("js-start-test.test-mode-multi")
    button.click()

    while driver.current_url == 'https://www.speedtest.net/':
        continue

    download = driver.find_element_by_class_name("result-data-large.number.result-data-value.download-speed")
    upload = driver.find_element_by_class_name("result-data-large.number.result-data-value.upload-speed")
    download_speed = download.get_attribute('innerHTML')
    upload_speed = upload.get_attribute('innerHTML')
    driver.quit()
    return(float(upload_speed), float(download_speed))

def speedtest_cli():
    down = os.popen('speedtest --no-upload')
    download = (down.read().split('Download: ')[1].split('Mbit/s')[0])
    up = os.popen('speedtest --no-download')
    upload = (up.read().split('Upload: ')[1].split('Mbit/s')[0])

    return(float(upload), float(download))