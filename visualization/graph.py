import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from visualization.count import *
from visualization.main import avg


def hangle():  # 한글 깨짐 처리
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


def tag_avg(happy_one, happy_tow, happy_three, sad_one, sad_tow, sad_three):
    happy_avg = [avg(
        letter_count(happy_one['content'].tolist())
        + letter_count(happy_tow['content'].tolist())
        + letter_count(happy_three['content'].tolist())
    ), avg(
        tag_count(happy_one['content'].tolist())
        + tag_count(happy_tow['content'].tolist())
        + tag_count(happy_three['content'].tolist())
    ), avg(
        emoji_count(happy_one['content'].tolist())
        + emoji_count(happy_tow['content'].tolist())
        + emoji_count(happy_three['content'].tolist())
    )]

    sad_avg = [avg(
        letter_count(sad_one['content'].tolist())
        + letter_count(sad_tow['content'].tolist())
        + letter_count(sad_three['content'].tolist())
    ), avg(
        tag_count(sad_one['content'].tolist())
        + tag_count(sad_tow['content'].tolist())
        + tag_count(sad_three['content'].tolist())
    ), avg(
        emoji_count(sad_one['content'].tolist())
        + emoji_count(sad_tow['content'].tolist())
        + emoji_count(sad_three['content'].tolist())
    )]

    avg_comparison_graph(sad_avg, happy_avg)


def create_graph(df):
    plt.scatter(df[0], df[1])
    plt.xlabel('tag_count')
    plt.ylabel('letter_count')
    plt.show()


def bar_graph(df, name):
    hangle()
    plt.title("기분 별 " + name)
    plt.bar(['#happy', '#sad'], df,
            width=0.5,
            color='grey')
    plt.ylabel(name)
    plt.show()


def plt_text_setting(x, df, b):
    for i, v in enumerate(x):
        if b:
            v = v + 0.4
        plt.text(v, df[i], df[i],  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize=9,
                 color='black',
                 horizontalalignment='center',  # horizontalalignment (left, center, right)
                 verticalalignment='bottom')


def avg_comparison_graph(sad, happy):
    hangle()
    x_label = ['letter_count', 'tag_count', 'emoji_count']
    x = pd.Series([1, 2, 3])

    plt.xticks(x + 0.2, x_label)

    plt.title('기분과 SNS의 연관관계')

    plt_text_setting(x, np.round(list(map(float, happy)), 2), False)
    plt_text_setting(x, np.round(list(map(float, sad)), 2), True)

    plt.bar(x, happy, color='yellow', width=0.4, label='#happy')
    plt.bar(x + 0.4, sad, color='skyblue', width=0.4, label='#sad')

    plt.legend()
    plt.show()


def letter_count_graph(sad_one, sad_tow, sad_t, happy_one, happy_tow, happy_three):
    plt.plot(sad_one, color='aquamarine')
    plt.plot(sad_tow, color='lightcyan')
    plt.plot(sad_t, color='skyblue')
    plt.plot(happy_one, color='pink')
    plt.plot(happy_tow, color='violet')
    plt.plot(happy_three, color='palevioletred')
    plt.show()


def happy_day_sad_day(happy, sad):
    hangle()

    plt.title('#행복한하루 #슬픈하루 글자 수 비교')
    plt.plot(happy, color='pink', label=avg(happy))
    plt.plot(sad, color='aquamarine', label=avg(sad))
    plt.legend(title='avg')
    plt.show()  # 선

    plt.title('#행복한하루 #슬픈하루 글자 수 비교')
    plt.scatter(range(100), happy, color='pink', label=avg(happy))
    plt.scatter(range(100), sad, color='aquamarine', label=avg(sad))
    plt.legend(title='avg')
    plt.show()  # 산점도


def all_scatter_hist(happy_one, happy_tow, happy_three,
                        sad_one, sad_tow, sad_three, title):  # 산점도와 히스토그램
    hangle()

    plt.title(title+' 사용 빈도 비교')
    plt.scatter(range(100), happy_one, color='pink')
    plt.scatter(range(100), happy_tow, color='pink')
    plt.scatter(range(100), happy_three, color='pink')
    plt.scatter(range(100), sad_one, color='aquamarine')
    plt.scatter(range(100), sad_tow, color='aquamarine')
    plt.scatter(range(100), sad_three, color='aquamarine')
    plt.show()  # 산점도

    plt.hist(x= range(100), weights=happy_one, bins = 50, label = '#행복해요', color = 'pink', alpha=0.5)
    plt.hist(x=range(100), weights=happy_tow, bins=50, label='#행복햄', color='violet', alpha=0.5)
    plt.hist(x=range(100), weights=happy_three, bins=50, label='#행복한하루', color='palevioletred', alpha=0.5)
    plt.hist(x=range(100), weights=sad_one, bins=50, label='#슬프다', color='aquamarine', alpha=0.5)
    plt.hist(x=range(100), weights=sad_tow, bins=50, label='#우울해', color='skyblue', alpha=0.5)
    plt.hist(x=range(100), weights=sad_three, bins=50, label='#슬픈하루', color='lightsteelblue', alpha=0.5)
    plt.title(title + ' 사용 빈도 비교')
    plt.legend(title='tag', loc = 'lower right')
    plt.show()


def emoji_and_tag(happy_one, happy_tow, happy_three, sad_one, sad_tow, sad_three): # 이모지랑 태그의 상관관계
    plt.subplot(221)
    # plt.scatter(range(100), tag_count_div(happy_one), color='pink')
    # plt.scatter(range(100), emoji_count(happy_one), color='blue')
    plt.plot(tag_count_div(happy_one))
    plt.plot(emoji_count(happy_one))

    plt.subplot(222)
    plt.plot(tag_count_div(happy_tow))
    plt.plot(emoji_count(happy_tow))

    plt.subplot(223)
    plt.plot(tag_count_div(sad_one))
    plt.plot(emoji_count(sad_one))

    plt.subplot(224)
    plt.plot(tag_count_div(sad_tow))
    plt.plot(emoji_count(sad_tow))

    plt.show()
