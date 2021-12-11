import numpy

from pandas import read_csv

from visualization.graph import *


def avg(s):
    return numpy.mean(s)


def choice_graph():
    happy_one = read_csv('../csv/happy_행복해요.csv', header='infer', encoding='utf-8')
    happy_tow = read_csv('../csv/happy_행복햄.csv', header='infer', encoding='utf-8')
    happy_three = read_csv('../csv/happy_행복한하루.csv', header='infer', encoding='utf-8')
    sad_one = read_csv('../csv/sad_슬프다.csv', header='infer', encoding='utf-8')
    sad_tow = read_csv('../csv/sad_우울해.csv', header='infer', encoding='utf-8')
    sad_three = read_csv('../csv/sad_슬픈하루.csv', header='infer', encoding='utf-8')

    num = int(input('1. csv 파일 평균\n2. 문자 수 비교 그래프\n3. #행복한하루 #슬픈하루 문자수 비교 그래프\n4. 이모지 갯수 비교 그래프\n5. 태그 개수 비교 그래프\n6. 이모티콘과 태그의 상관관계\n'))

    if num == 1:  # csv 파일 평균
        tag_avg(happy_one, happy_tow, happy_three, sad_one, sad_tow, sad_three)
    elif num == 2:  # 문자 수 비교
        letter_count_graph(letter_count(sad_one['content'].tolist()),
                           letter_count(sad_tow['content'].tolist()),
                           letter_count(sad_three['content'].tolist()),
                           letter_count(happy_one['content'].tolist()),
                           letter_count(happy_tow['content'].tolist()),
                           letter_count(happy_three['content'].tolist()))
    elif num == 3:  # 행복한하루와 슬픈하루 태그
        happy_day_sad_day(letter_count(happy_three['content'].tolist()), letter_count(sad_three['content'].tolist()))
    elif num == 4:  # 이모지 갯수 비교
        all_scatter_hist(emoji_count(happy_one['content'].tolist()),
                         emoji_count(happy_tow['content'].tolist()),
                         emoji_count(happy_three['content'].tolist()),
                         emoji_count(sad_one['content'].tolist()),
                         emoji_count(sad_tow['content'].tolist()),
                         emoji_count(sad_three['content'].tolist()),
                         '이모지')
    elif num == 5:  # 태그 개수 비교
        all_scatter_hist(tag_count(happy_one['content'].tolist()),
                         tag_count(happy_tow['content'].tolist()),
                         tag_count(happy_three['content'].tolist()),
                         tag_count(sad_one['content'].tolist()),
                         tag_count(sad_tow['content'].tolist()),
                         tag_count(sad_three['content'].tolist()),
                         '태그')
    elif num == 6:  # 이모티콘과 태그의 상관관계
        emoji_and_tag(happy_one['content'].tolist(),
                      happy_tow['content'].tolist(),
                      happy_three['content'].tolist(),
                      sad_one['content'].tolist(),
                      sad_tow['content'].tolist(),
                      sad_three['content'].tolist())


if __name__ == '__main__':
    choice_graph()
