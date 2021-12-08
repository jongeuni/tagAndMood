import time
from bs4 import BeautifulSoup


# 따라서 특정 검색어에 따른 주소
def insta_searching(word):
    url = "http://www.instagram.com/explore/tags/" + word
    return url


# 첫 번째 페이지 클릭
def select_first(driver):
    first = driver.find_element_by_css_selector(
        '#react-root > div > div > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0')

    first.click()
    time.sleep(3)


# 다음 페이지로 넘어가는 코드
def move_next(driver):
    right = driver.find_element_by_css_selector(
        'body > div._2dDPU.QPGbb.CkGkG > div.EfHg9 > div > div > div.l8mY4.feth3 > button')
    time.sleep(10)
    right.click()
    time.sleep(3)


# 정보 저장
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 본문 내용
    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
        content = ' '
    # 작성일자
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

    data = [content, date]

    return data
