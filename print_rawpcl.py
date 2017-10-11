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

import os
import sys
import io
import time
import win32print


def remove_silently(file1):
    """Removing silently files from last time if there are any left"""
    try:
        os.remove(file1)
    except OSError:
        pass

# Asign your printers
first_default_printer = win32print.GetDefaultPrinter()

# If there is command line argument, the first one is our file_to_print
if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    file_to_print = "RACUN.TXT"
 
# Printing RAW data to the default printer
try:
    # rb --> 'read, bytes', string is 'bytes' type, not unicode (Python3)
    with io.open(file_to_print, 'r') as f:
        raw_data = f.read()
        hPrinter = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, (
                    "print_rawpcl.py data", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, raw_data)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
except OSError as e:
    print("Failed: {}".format(e))

# Message at the end of execution
print("Script finished successfully. Everything OK!")
time.sleep(2)  # Wait 2 seconds for reader to read
