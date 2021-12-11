import re
import emoji


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


def tag_count_div(c):
    tag_count_lis = []
    for i in c:
        tags = re.findall(r'#[^\s#,\\]+', i)
        tag_count_lis.append(len(tags)/2.5)
    return tag_count_lis
