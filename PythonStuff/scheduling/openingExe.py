import subprocess
import os
subprocess.Popen('C:\\Windows\\notepad.exe')

# passing cmd args
subprocess.Popen([
    'C:\\Windows\\notepad.exe',
    os.path.realpath('files/mytext.txt')
])
