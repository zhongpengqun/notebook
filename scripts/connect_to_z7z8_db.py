# coding: utf-8
import psycopg2
import subprocess
import requests
import os
import time

import sys
from importlib import reload


reload(sys)
#sys.setdefaultencoding('utf8')

connect = psycopg2.connect(dbname='jiya', user='postgres', password='postgres', host='139.196.39.92', port=6432)
cur = connect.cursor()
# cur.execute("select spell, short_meaning, meaning, soramimi from words where spell='consider';")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

def play_sound(path):
    os.system('afplay '+path)

def download_and_play_word_mp3(word):
    r = requests.get('http://english.z7z8.cc/word/sound/?word={}'.format(word))
    f=open('/Users/vzhong/Downloads/z7z8.mp3', 'wb+')
    f.write(r._content)
    f.close()

    play_sound('/Users/vzhong/Downloads/z7z8.mp3')

def read_from_clipboard():
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

current_clipboard_content = ''

while True:
    clipboard_content = read_from_clipboard()
    if clipboard_content != current_clipboard_content:
        # with open('/Users/vzhong/clip_board_content_%s.txt'%str(int(time.time())), 'a') as f:
        #     f.write(clipboard_content)
        # print(clipboard_content)
        cur.execute("""select spell, short_meaning, meaning, soramimi from words where spell='{}';""".format(clipboard_content))
        rows = cur.fetchall()
        for row in rows:
            print(row[0])
            print(row[2])
            print(row[3])
            print('')
            download_and_play_word_mp3(row[0])
        current_clipboard_content = clipboard_content

    time.sleep(1)
