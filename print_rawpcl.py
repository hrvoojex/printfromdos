#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T
Last edit: June 2017

'pip install pypiwin32 --> for installing win32api'
In python 2: 'python -m pip install pypiwin32'
io module for io.open in Python2, the same as 'open' in Python3
First command line argument is for file name which we want to print:
'python print_rawpcl.py my_pcl_text_file.txt'
"""

import os, sys, io, win32print, win32api, subprocess


def remove_silently(file1):
    """Removing silently files from last time if there are any left"""
    try:
        os.remove(file1)
    except OSError:
        pass

# Asign your printers and variables
first_default_printer = win32print.GetDefaultPrinter()
tmp_printer = "local_pcl"
my_pcl_file = "print.pcl"
my_output_pdf = "print.pdf"

# Remove files if they already exist
remove_silently(my_output_pdf)
remove_silently(my_pcl_file)

# If there is command line argument, the first one is our file_to_print
if len(sys.argv) > 1:
    file_to_print = sys.argv[1]
else:
    file_to_print = "RACUN.TXT"

# Searching for supported PCL printers as default printer
pcl_supported = False
supported_printers = ["2035", "1320", "KONICA", "DIREKT"]
for item in supported_printers:
    if item.lower() in first_default_printer.lower():
        pcl_supported = True
        break
    else:
        is_supported = False

if pcl_supported == False:
        win32print.SetDefaultPrinter(tmp_printer)

# Printing RAW data to the virtual 'local_pcl' printer or to the 'HP LJ P2035'
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

# Convert a pcl file to pdf with WinPCLtoPDF.exe
# if the default printer is local_pcl
converter_app = "WinPCLtoPDF.exe"
if win32print.GetDefaultPrinter() == "local_pcl":
    subprocess.call([converter_app, my_pcl_file])

    # return default printer to the printer that was default at the start
    win32print.SetDefaultPrinter(first_default_printer)

    # Finally, print that print.pdf to your first default printer silently
    gsprint_app = "C:\\Program Files\\Ghostgum\\gsview\\gsprint.exe"
    p = subprocess.Popen(
            [gsprint_app, my_output_pdf],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Waits for the gs process to end
    stdout, stderr = p.communicate()
    # Remove print.pcl and print.pdf file
    remove_silently(my_output_pdf)
    remove_silently(my_pcl_file)

# Removes that first txt file
remove_silently(file_to_print)
