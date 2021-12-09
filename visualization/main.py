import emoji
import pandas as pd
import re


def emoji_count(c):  # 이모지 갯수 새기!
    emoji_count_lis = []
    for i in c:
        emoji_count_lis.append(emoji.emoji_count(i))
    return emoji_count_lis


def letter_count(c):  # 글자 수 새기!
    letter_count_lis = []

    for i in c:
        letter_count_lis.append(len(i))

    return letter_count_lis


def tag_count(c):  # 태그 수 새기!
    tag_count_lis = []
    for i in c:
        tags = re.findall(r'#[^\s#,\\]+', i)
        tag_count_lis.append(len(tags))
    return tag_count_lis


if __name__ == '__main__':
    # row = ['content', 'date', 'tag_count', 'letter_count', 'imoji_count']
    df = pd.read_csv('../csv/happy_행복한하루.csv', header='infer', encoding='utf-8')  # DataFrame
    content = df['content'].tolist()
    fi = pd.DataFrame({
        'content' : df['content'].tolist(),
        'date' : df['data'].tolist(),
        'tag_count':tag_count(content),
        'letter_count':letter_count(content),
        'emoji_count':emoji_count(content)
    })
    print(fi)

