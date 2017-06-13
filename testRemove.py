#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for removing a file in Windows and Linux"
"""

import sys
import os

myFile = sys.argv[1]
os.remove(myFile)

