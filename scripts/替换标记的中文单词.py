# coding: utf-8
import re
import os

journals_file_path = os.getcwd() + "/raw/journals.md"
journals_file_fined_path = os.getcwd() + "/docs/journals.md"
existed_cn_words = {}
fanyi_file_path = os.getcwd() + "/scripts/查找标记了在中文单词--翻译.txt"

original_text = ""

with open(journals_file_path, 'r') as f:
    original_text = "".join(f.readlines())

with open(fanyi_file_path, 'r') as f:
    for x in f.readlines():
        x = x.replace('\n', '')
        cn, translation = x.split(':')
        # print('-----')
        # print('\#{}\#'.format(cn))
        # print('======')
        if translation:
            original_text = original_text.replace('{}'.format(cn), '{}(<u>{}</u>)'.format(cn, translation))

with open(journals_file_fined_path, 'w') as f:
    f.write(original_text)
    f.close()