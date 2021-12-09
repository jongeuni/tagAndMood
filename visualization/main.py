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

    return letter_count_lis


def tag_count(c):
    tag_count_lis = []
    for i in c:
        tags = re.findall(r'#[^\s#,\\]+', i)
        tag_count_lis.append(len(tags))
    return tag_count_lis


def evg(s):
    print(s)
    return numpy.mean(s)


def graph_choice():
    print()


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
