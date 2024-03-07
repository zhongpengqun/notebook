import os
import re
import glob
import time
import yaml
import platform
import re

import sqlite3
from init import init_db, init_table, DB, TABLE
from common_functions import read_from_clipboard


RELATED_LINES_UP_COUNT = 8
RELATED_LINES_DOWN_COUNT = 15


current_clipboard_content = ""

pt = platform.platform()


# >>> ireplace('hippo?', 'giraffe!?', 'You want a hiPPO?')
# 'You want a giraffe!?'
def ireplace(old, repl, text):
    return re.sub('(?i)'+re.escape(old), lambda m: repl, text)


def highlight_matched_substr(targetline, substr):
    result_chars = []
    current_targetline_index = 0

    for index, char in enumerate(targetline):
        if index < current_targetline_index:
            continue
        if targetline[index: index + len(substr)].lower() == substr.lower():
            result_chars.append(f'\033[92m{targetline[current_targetline_index: current_targetline_index + len(substr)]}\033[0m')
            current_targetline_index += len(substr)
        else:
            result_chars.append(char)
            current_targetline_index += 1
        
    return ''.join(result_chars)


def print_keyword_related_note(keyword):
    result = []

    if keyword:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute(f"select id, file, content from {TABLE} where LOWER(content) like ?;", ("%" + keyword.lower() + "%",))
        matched_records = cursor.fetchall()

        for _matched_record in matched_records:
            _id, _file, _content = _matched_record
            result.append(f"\033[1;33;40m------- Found in file: {_file} ↓↓↓\033[0m")

            # 匹配行的上下5行也将被选中显示出来
            selected_lines_ids = list(range(max(1,_id - RELATED_LINES_UP_COUNT), _id + RELATED_LINES_UP_COUNT))
            cursor.execute("select content from %s where id in (%s);" % (TABLE, ','.join([str(_) for _ in selected_lines_ids])))
            selected_lines = cursor.fetchall()

            for _selected_line in selected_lines:
                line_content = _selected_line[0]
                highlighted_line = highlight_matched_substr(line_content, keyword)
                result.append(highlighted_line)


    print('\n'.join(result))


# all_lines_lower = [x.lower() for x in all_lines]

# test_str = '扛'
# test_str = read_from_clipboard()

current_keyword = ''

init_db()
init_table()


while True:
    clipboard_content = read_from_clipboard()

    if clipboard_content != current_keyword:
        print('\n\n\n\n')
        if "Windows" in pt:
            os.system('CLS')
        else:
            os.system('clear')
        print('========== RESULT ==========')
        print_keyword_related_note(clipboard_content)
        current_keyword = clipboard_content
    time.sleep(2)
