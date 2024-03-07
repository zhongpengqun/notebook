# coding: utf-8
import time

clipboard_content_save_at = '/tmp/clipboard.txt'


def read_from_clipboard():
    import subprocess
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')


if __name__ == "__main__":
    while 1:
        clipboard_content = read_from_clipboard()
        with open(clipboard_content_save_at, 'w') as f:
            f.write(clipboard_content)
        time.sleep(1)