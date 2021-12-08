import csv
import pandas as pd
import re


def imoji_count():  # 이모지 갯수 새기!
    print('hi')


def content_count():  # 글자 수 새기!
    print('hi')


def tag_count(c):  # 태그 수 새기!
    tag_count_lis = []
    for i in c:
        tags = re.findall(r'#[^\s#,\\]+', i)
        tag_count_lis.append(len(tags))
    return tag_count_lis


if __name__ == '__main__':
    df = pd.read_csv('../csv/happy_행복한하루.csv', header='infer', encoding='utf-8')  # DataFrame
    content = df['content'].tolist()
    print(tag_count(content))

