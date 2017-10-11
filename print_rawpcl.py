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
import subprocess
import webbrowser


def remove_silently(file1):
    """Removing silently files from last time if there are any left"""
    try:
        os.remove(file1)
    except OSError:
        pass

# Assign a variables for converting a PCL file to pdf with
# GhostPCL (Ghostscript) if the default printer is virtual 'local_pcl'
converter_app = 'C:/Python34/WinPCLtoPDF.exe'
myPCLfile = 'C:/SMECE/print.pcl'
myPDFfile = 'C:/SMECE/print.pdf'

# Remove those files if they exist from previous script execution
remove_silently(myPCLfile)
remove_silently(myPDFfile)

# Asign your printers
first_default_printer = win32print.GetDefaultPrinter()
tmp_printer = "local_pcl"

# If there is command line argument, the first one is our file_to_print
if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    file_to_print = "RACUN.TXT"

# #Commented this out on 10.10.2017. Everything goes to pdf now.
#
# #Searching for supported PCL printers as default printer
# pcl_supported = False
# supported_printers = ["2035", "1320", "KONICA", "DIREKT"]
# for item in supported_printers:
#    if item.lower() in first_default_printer.lower():
#        pcl_supported = True
#        break
#
# #If our printer doesn't support PCL, we declare virtual local_pcl printer
# #as default one and create .pcl file
# if not pcl_supported:
#        win32print.SetDefaultPrinter(tmp_printer)
#
# #Declare virtual printer 'local_pcl' as default one
win32print.SetDefaultPrinter(tmp_printer)
 
# Printing RAW data to the default printer
try:
    # rb --> 'read, bytes', string is 'bytes' type, not unicode (Python3)
    with io.open(file_to_print, 'rb') as f:
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

if win32print.GetDefaultPrinter() == "local_pcl":
    subprocess.call([converter_app, myPCLfile])
    win32print.SetDefaultPrinter(first_default_printer)
    webbrowser.open('file://' + os.path.realpath(myPDFfile))

# Message at the end of execution
print("Script finished successfully. Everything OK!")
time.sleep(2)  # Wait 2 seconds for reader to read
