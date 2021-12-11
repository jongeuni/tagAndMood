import emoji
import numpy
import pandas as pd
import re

from pandas import read_csv
from visualization.graph import create_graph, bar_graph


def emoji_count(c):
    emoji_count_lis = []
    for i in c:
        emoji_count_lis.append(emoji.emoji_count(i))
    return emoji_count_lis


def letter_count(c):
    letter_count_lis = []

    for i in c:
        letter_count_lis.append(len(i))

def avg(s):
    return numpy.mean(s)


def graph_choice():
    print()


def choice_graph():
    happy_one = read_csv('../csv/happy_행복해요.csv', header='infer', encoding='utf-8')
    happy_tow = read_csv('../csv/happy_행복햄.csv', header='infer', encoding='utf-8')
    happy_three = read_csv('../csv/happy_행복한하루.csv', header='infer', encoding='utf-8')
    sad_one = read_csv('../csv/sad_슬프다.csv', header='infer', encoding='utf-8')
    sad_tow = read_csv('../csv/sad_우울해.csv', header='infer', encoding='utf-8')
    sad_three = read_csv('../csv/sad_슬픈하루.csv', header='infer', encoding='utf-8')

    num = 4

    if num == 1: # csv 파일 평균
        tag_avg()
    elif num == 2: #
        letter_count_graph(letter_count(sad_one['content'].tolist()),
                           letter_count(sad_tow['content'].tolist()),
                           letter_count(sad_three['content'].tolist()),
                           letter_count(happy_one['content'].tolist()),
                           letter_count(happy_tow['content'].tolist()),
                           letter_count(happy_three['content'].tolist()))
    elif num == 3: # 행복한하루와 슬픈하루 태그
        happy_day_sad_day(letter_count(happy_three['content'].tolist()), letter_count(sad_three['content'].tolist()))
    elif num == 4:
        all_emoji_dot_graph(emoji_count(happy_one['content'].tolist()), emoji_count(happy_tow['content'].tolist()), emoji_count(happy_three['content'].tolist()),
                            emoji_count(sad_one['content'].tolist()), emoji_count(sad_tow['content'].tolist()), emoji_count(sad_three['content'].tolist()))


def tag_avg():
    happy_day = read_csv('../csv/happy_행복한하루.csv', header='infer', encoding='utf-8')
    happy_ham = read_csv('../csv/happy_행복햄.csv', header='infer', encoding='utf-8')
    sad_day = read_csv('../csv/sad_슬픈하루.csv', header='infer', encoding='utf-8')
    sad_uu = read_csv('../csv/sad_우울해.csv', header='infer', encoding='utf-8')

    happy_avg = [avg(
        letter_count(happy_day['content'].tolist())
        + letter_count(happy_ham['content'].tolist())
    ), avg(
        tag_count(happy_day['content'].tolist())
        + tag_count(happy_ham['content'].tolist())
    ), avg(
        emoji_count(happy_day['content'].tolist())
        + emoji_count(happy_ham['content'].tolist())
    )]

    sad_avg = [avg(
        letter_count(sad_day['content'].tolist())
        + letter_count(sad_uu['content'].tolist())
    ), avg(
        tag_count(sad_day['content'].tolist())
        + tag_count(sad_uu['content'].tolist())
    ), avg(
        emoji_count(sad_day['content'].tolist())
        + emoji_count(sad_uu['content'].tolist())
    )]

    avg_comparison_graph(sad_avg, happy_avg)


if __name__ == '__main__':
    choice_graph()
