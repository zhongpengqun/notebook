# coding: utf-8
import re
import os

journals_file_path = os.getcwd() + "/raw/journals.md"
existed_cn_words = {}
fanyi_file_path = os.getcwd() + "/scripts/查找标记了在中文单词--翻译.txt"

def all_text():
    f = open(journals_file_path, 'r')
    return "".join(f.readlines())

def get_existed_cn_words():
    f = open(fanyi_file_path, 'r')
    lines = f.readlines()
    for cn_word_and_translation in lines:
        print('=======')
        cn_word_and_translation = cn_word_and_translation.replace('\n', '')
        cn_word = cn_word_and_translation.split(":")[0]
        existed_cn_words[cn_word] = cn_word_and_translation.split(":")[1]


get_existed_cn_words()

text = all_text()
# marked_cn_words = re.findall(r'\\#([\u4e00-\u9fa5]+)\\#', text)
marked_cn_words = re.findall(r'([\u4e00-\u9fa5]+)', text)

will_append_text = ""

for marked_cn_word in marked_cn_words:
    if marked_cn_word not in existed_cn_words.keys():
        will_append_text += marked_cn_word + ":\n"

will_append_text = list(set(will_append_text.split('\n')))
print(will_append_text)

with open(fanyi_file_path, 'a') as f:
    will_append_text_str = '\n'.join(will_append_text)
    f.write(will_append_text_str)
    f.close()
