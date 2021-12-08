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