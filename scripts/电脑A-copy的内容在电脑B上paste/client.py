#import os
#import subprocess
#
#command = [
#    "sshpass",
#    "-p",
#    "Xs123456!@#$%^", # Assuming the password is provided through an env variable.
#    "ssh",
#    "vzhong@192.168.0.103",
#    "cat /tmp/clipboard.txt",
#]
#
#subprocess.run(command)


import os
import clipboard

file_path = '/tmp/clipboard.txt'


def copy_to_clipboard():
    os.system(f'sshpass -p "Xs123456!@#$%^" scp vzhong@192.168.0.103:{file_path} /tmp/')

    with open(file_path, 'r') as f:
        clipboard_content = f.readlines()
        clipboard_content = ''.join(clipboard_content)
        clipboard.copy(clipboard_content)


copy_to_clipboard()