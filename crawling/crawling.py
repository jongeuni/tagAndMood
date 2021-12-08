import time
import re
from bs4 import BeautifulSoup


# 나중에 하기 버튼
def later_button(driver):
    # 나중에 하기1
    later_1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div/div/button')
    later_1.click()
    time.sleep(3)

    # 나중에 하기2
    later_2 = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    # later_2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
    later_2.click()
    time.sleep(2)


# 따라서 특정 검색어에 따른 주소
def insta_searching(word):
    url = "http://www.instagram.com/explore/tags/" + word
    return url


#첫 번째 페이지 클릭
def select_first(driver):
    first = driver.find_element_by_css_selector('#react-root > div > div > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0')
    first.click()
    time.sleep(3)
