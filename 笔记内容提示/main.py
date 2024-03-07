import os
import re
import glob
import time
import yaml



RELATED_LINES_UP_COUNT = 5
RELATED_LINES_DOWN_COUNT = 10
SETTINGS_FILE_PATH = os.path.abspath(os.path.join(os.getcwd(), "settings.yml"))

with open(SETTINGS_FILE_PATH, "r") as f:
    settings = yaml.full_load(f)

all_lines = []

current_clipboard_content = ""

def read_from_clipboard():
    import subprocess
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def get_all_lines():
    for document_dir in settings.get('document_dirs'):
        for path, subdirs, files in os.walk(document_dir):
            for name in files:
                if not name.endswith(tuple(settings.get('extensions'))):
                    continue
                with open(f'{path}/{name}') as f:
                    for _line in f.readlines():
                        all_lines.append(_line)

get_all_lines()


def print_keyword_related_note(keyword):
    result = []

    for _i, _line in enumerate(all_lines):
        if keyword.lower() in _line.lower():
            all_lines[_i] = all_lines[_i].replace(keyword, f'\033[92m{keyword}\033[0m')
            item = '\n'.join(all_lines[_i - RELATED_LINES_UP_COUNT : _i + RELATED_LINES_DOWN_COUNT])
            result.append(item)

    print('\n----------------------------------------\n'.join(result[:5]))

# all_lines_lower = [x.lower() for x in all_lines]

# test_str = '扛'
# test_str = read_from_clipboard()

current_keyword = ''

while True:
    clipboard_content = read_from_clipboard()
    if clipboard_content != current_keyword:
        print('\n\n\n\n')
        os.system('clear')
        print('========== RESULT ==========')
        print_keyword_related_note(clipboard_content)
        current_keyword = clipboard_content
    time.sleep(2)
