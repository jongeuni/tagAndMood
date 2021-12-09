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
    num = int(input('몇 개의 csv 파일을 가져올까요?'))
    csv_files = []
    dfs = []
    tags_evg = []
    for i in range(0, num):
        file_name = input('가져올 csv 파일의 이름을 말해주세요')
        csv_files.append(read_csv('../csv/' + file_name + '.csv', header='infer', encoding='utf-8'))
        content = csv_files[i]['content'].tolist()

        dfs.append(pd.DataFrame({
            'content': csv_files[i]['content'].tolist(),
            'date': csv_files[i]['data'].tolist(),
            'tag_count': tag_count(content),
            'letter_count': letter_count(content),
            'emoji_count': emoji_count(content)
        }))

        tags_evg.append(
            evg(tag_count(content))
        )

    print(tags_evg)
    bar_graph(tags_evg, 'tag 평균 수')
    # create_graph(tags_evg)
