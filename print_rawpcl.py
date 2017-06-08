import os, sys
import win32print
import io
printer_name = win32print.GetDefaultPrinter()

# Autor: Hrvoje T
# Last edit: June 2017
# pip instal reportlab
# pip install pypiwin32 --> win32api, za python 2 ide python -m pip install 
# io module, io.open

# ako postoje argumenti komandne linije,
# prvi argument je ime datoteke za print
if len(sys.argv) > 1:
  file_to_print = sys.argv[1]
else:
  file_to_print = "RACUN.TXT"
try:
  # rb - read, bytes
  with io.open(file_to_print,'rb') as f:
    raw_data = f.read()
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
      hJob = win32print.StartDocPrinter(hPrinter, 1,("test of raw data", None, "RAW"))
      try:
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, raw_data)
        win32print.EndPagePrinter(hPrinter)
      finally:
        win32print.EndDocPrinter(hPrinter)
    finally:
      win32print.ClosePrinter(hPrinter)
  # uklanja datoteke nakon printanja istih
  os.remove(file_to_print)
except:
  print("Nisu zadani argumenti programa 'print_rawpcl.py':\n \
        - datoteka za štampanje nakon imena programa ne postoji\n \
        - osnovna datoteka RACUN.TXT za štampanje ne postoji ")
  

