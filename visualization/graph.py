import matplotlib.pyplot as plt
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


def avg_comparison_graph(sad, happy):
    hangle()
    x_label = ['emoji_count', 'tag_count', 'letter_count']
    x = pd.Series([1, 2, 3])

    plt.xticks(x + 0.2, x_label)

    plt.bar(x, happy, color='yellow', width=0.4, label='#happy')
    plt.bar(x + 0.4, sad, color='skyblue', width=0.4, label='#sad')

    plt.legend()
    plt.show()
