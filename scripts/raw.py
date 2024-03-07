# coding: utf-8

with open('/Users/vzhong/Documents/zhongpengqun.github.io/ingore-it/raw.txt') as f:
    _content = f.readlines()

content = ''.join(_content)
content = content.replace('\n', '')

content = content.replace('Mr.', 'Mr ')
content = content.replace('.', '.\n')

print(content)
