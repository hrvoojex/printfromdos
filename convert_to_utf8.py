#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert a document to a document with UTF-8 encoding.
The first argument is a file name and the second argument
is a coding point eg. 852, cp1252 etc.

python convert_to_utf8.py my_table.csv ibm852

Author: Hrvoje T
Last edit: June 2017.
"""

import sys
import io

try:
    # command line arguments
    input_file = sys.argv[1]
    my_encoding = sys.argv[2]
    
    with io.open(input_file,'r',encoding=my_encoding) as f:
        data = f.read()
        
    with io.open(input_file,'w',encoding='utf8') as f:
        f.write(data)
except:
    print("Wrong arguments: file name (1) and/or encoding (2)")
    sys.exit()
print("OK, successfully converted to UTF-8!")
