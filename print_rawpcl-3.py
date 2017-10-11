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

#import os
import sys
#import io
#import win32print
#import win32ui


#printer_name = win32print.GetDefaultPrinter()

if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    file_to_print = "RACUN.TXT"

# try:
# # rb je za 'read, bytes', string je byte ne enkodiran tekst
#     with io.open(file_to_print,'rb') as f:
#         raw_data = f.read()
#         hPrinter = win32print.OpenPrinter(printer_name)
#         try:
#             hJob = win32print.StartDocPrinter(hPrinter, 1,("print_rawpcl.py data", None, "RAW"))
#             try:
#                 win32print.StartPagePrinter(hPrinter)
#                 win32print.WritePrinter(hPrinter, raw_data)
#                 win32print.EndPagePrinter(hPrinter)
#             finally:
#                 win32print.EndDocPrinter(hPrinter)
#         finally:
#             win32print.ClosePrinter(hPrinter)
#     # uklanja datoteke nakon printanja istih
#     os.remove(file_to_print)
# except OSError as e:
#     print("Pojavila se greška: {}".format(e))

# with open(file_to_print, "rb") as f:
#     my_raw_data = f.read()
#     # X from the left margin, Y from top margin
#     # both in pixels
#     X=50; Y=50
#     multi_line_string = my_raw_data.split()
#     hDC = win32ui.CreateDC ()
#     hDC.CreatePrinterDC (printer_name)
#     hDC.StartDoc ("raw data from python script")
#     hDC.StartPage ()
#     for line in multi_line_string:
#          hDC.TextOut(X,Y,line)
#          Y += 100
#     hDC.EndPage ()
#     hDC.EndDoc ()

import win32ui
import win32print
import win32con

INCH = 1440

with open(file_to_print, "r") as f:
    my_raw_data = f.read()
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
    hDC.StartDoc(my_raw_data)
    hDC.StartPage()
    hDC.SetMapMode(win32con.MM_TWIPS)
    hDC.DrawText("TEST", (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
    hDC.EndPage()
    hDC.EndDoc()