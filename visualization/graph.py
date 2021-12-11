import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def hangle():  # 한글 깨짐 처리
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


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


def all_emoji_graph(happy_one, happy_tow, happy_three,
                        sad_one, sad_tow, sad_three):  # 이모지 그래프
    hangle()
    plt.title('이모티콘 사용 빈도 비교')
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
    plt.title('이모티콘 사용 빈도 비교')
    plt.legend(title='tag')
    plt.show()
