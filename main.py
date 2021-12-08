import os.path

from selenium import webdriver
import pandas as pd

from crawling.crawling import *
from env import env_setting


def crawling():
    word = "슬픔"
    url = insta_searching(word)

    driver.get(url)
    time.sleep(8)

    select_first(driver)

    results = []

    target = 500
    for i in range(target):
        try:
            data = get_content(driver)
            print(data)
            results.append(data)
            move_next(driver)
        except:
            time.sleep(2)
            move_next(driver)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    word = '슬픔'

    # url = insta_searching(word)
    # driver.get(url)
    # time.sleep(4)

    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    env_setting()

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)

    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(password)
    time.sleep(5)
    input_pw.submit()

    time.sleep(5)

    later_button(driver)

    # crawling()
