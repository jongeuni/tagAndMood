from selenium import webdriver
import pandas as pd

from crawler.crawling import *
from crawler.login import login


def crawling(word):
    url = insta_searching(word)

    driver.get(url)
    time.sleep(8)

    select_first(driver)

    results = []

    target = 100  # 크롤링 할 글 갯수

    for i in range(target):
        try:
            data = get_content(driver)
            results.append(data)
            move_next(driver)
        except:
            time.sleep(2)
            move_next(driver)

    print(results)
    results_df = pd.DataFrame(results)
    print(results_df)
    results_df.columns = ['content', 'data']
    print(results_df)
    results_df.to_csv('../csv/happy_행복한하루.csv', encoding='utf-8-sig', index=False)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    _word = input('어떤 태그에 대한 크롤링을 진행할까요?')

    driver.get('https://www.instagram.com/accounts/login/')

    login(driver)  # 인스타그램에 로그인

    crawling(_word)
