#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print a file to a default printer

author: Hrvoje T
last edited: June 2017
"""

import os
import sys
import subprocess
#import win32print

if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.stdin.write("This is print test sentence")
elif sys.platform == "darwin":
    # MAC OS X
    pass
elif sys.platform == "win32":
    # Windows
    os.startfile("C:/tmp/tmp.txt", "print")
