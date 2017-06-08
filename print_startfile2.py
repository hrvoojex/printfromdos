#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print a file to a default printer
last edited: June 2017
"""
import os
import sys
import subprocess
#import win32print

filepath = 'tmp.txt'
if os.path.isfile(filepath):
    if sys.platform == "linux" or sys.platform == "linux2":
        # linux
        lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        with open(filepath,'r') as file:
            lpr.stdin.write(file.read())

    elif sys.platform == "darwin":
        # MAC OS X
        pass
    elif sys.platform == "win32":
        # Windows
        os.startfile(filepath, "print")
else:
    print("No file named: {}".format(filepath))
