#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T.
Last edit: 11.10.2017.
Version: 1.0.4

'pip install pypiwin32 --> for installing win32print'
In python 2: 'python -m pip install pypiwin32'
io module for io.open in Python2, the same as 'open' in Python3

First command line argument is for file name which we want to print:
'python print_rawpcl.py myPCLfile.txt'
"""

import sys
import time
import win32api
import win32print
import winreg
import subprocess


my_encoding = "cp852"

def notepad_print(textfile, newset=None):
    if newset is not None:
        oldset = {}
        hkcu = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        notepad = winreg.OpenKey(hkcu, r'Software\Microsoft\Notepad', 0,
                                 winreg.KEY_ALL_ACCESS)
        for key, item in newset.items():
            oldset[key] = winreg.QueryValueEx(notepad, key)
            winreg.SetValueEx(notepad, key, None, item[1], item[0])

    # force printing with notepad, instead of using the 'print' verb
    win32api.ShellExecute(0, 'open', 'notepad.exe', '/p ' + textfile, '.', 0)
    #win32api.ShellExecute(0, 'print', textfile, None, '.', 0)
    #subprocess.call(['notepad', '/p', textfile])
    # win32api.ShellExecute(0,
    #                       'print',
    #                       textfile,
    #                       '/d:"%s"' % win32print.GetDefaultPrinter(),
    #                       '.',
    #                       0)

    input('once the job is queued, hit <enter> to continue')

    if newset is not None:
        for key, item in oldset.items():
            winreg.SetValueEx(notepad, key, None, item[1], item[0])

# If there is command line argument, the first one is our file_to_print
if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    print("No input file")
    sys.exit()

try:
    with open(file_to_print, "rb") as f:
        raw_data = f.read()
        raw_data_unicode = raw_data.decode(my_encoding)
        raw_data = raw_data_unicode.encode("utf-8")

    filename = "C:\SMECE\print.txt"
    with open(filename, "wb") as d:
        d.write(raw_data)

    notepad_print(filename, {'szHeader': ('', 1), 'szTrailer': ('', 1)})

except OSError as e:
    print("Failed: {}".format(e))

print("Script ended. Everything OK!")
time.sleep(2)
