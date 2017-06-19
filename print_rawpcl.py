#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Autor: Hrvoje T
Last edit: June 2017
pip instal reportlab
pip install pypiwin32 --> win32api, za python 2 ide python -m pip install 
io module, io.open
ako postoje argumenti komandne linije,
prvi argument je ime datoteke za print
"""

import os
import sys
import io
import win32print
import subprocess


first_default_printer = win32print.GetDefaultPrinter()
tmp_printer = "local_pcl"

if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    file_to_print = "RACUN.TXT"

if "2035" in first_default_printer:
    # do nothing if a printer is supporting PCL
    pass
else:
    # if the printer is not supporting PCL and can't print RAW data
    # change default printer to local_pcl 
    win32print.SetDefaultPrinter(tmp_printer)
    
try:
# rb je za 'read, bytes', string je byte ne enkodiran tekst
    with io.open(file_to_print,'rb') as f:
        raw_data = f.read()
        hPrinter = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1,("print_rawpcl.py data", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, raw_data)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
    # uklanja datoteke nakon printanja istih
    #os.remove(file_to_print)
except OSError as e:
    print("Pojavila se greška: {}".format(e))
    
# return default printer to the printer before running this script
win32print.SetDefaultPrinter(first_default_printer)
