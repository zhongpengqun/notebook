import platform

# import win32clipboard
import pyperclip


RELATED_LINES_UP_COUNT = 5
RELATED_LINES_DOWN_COUNT = 10


current_clipboard_content = ""

pt = platform.platform()


def read_from_clipboard():
    if "Windows" in pt:
        data = pyperclip.paste()
        return data
    else:
        import subprocess
        return subprocess.check_output(
            'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
