# coding: utf-8
import nltk
import jieba


# text_location = "/Users/vzhong/Documents/zhongpengqun.github.io/ingore-it/中国共产党章程.txt"
text_location = "游行示威法.txt"


def read_text(text_location):
    with open(text_location, 'r') as f:
        text = ''.join(f.readlines())
    # print(text)
    return text


text = read_text(text_location)


cns = jieba.lcut(text)
# print(text)
# cns = jieba.lcut('hello world')

cns = list(set(cns))

for _cn in cns:
    print(_cn)

print(len(cns))
# print([_cn for _cn in cns])
