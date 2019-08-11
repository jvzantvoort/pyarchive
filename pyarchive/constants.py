#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""constants.py - $description


Copyright (C) 2019 John van Zantvoort

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import os

__author__ = "John van Zantvoort"
__copyright__ = "JDC"
__email__ = "john@vanzantvoort.org"
__license__ = "MIT"

APPNAME = 'pyarchive'

APPDIR = os.path.join("~", "." + APPNAME)
APPDIR = os.path.expanduser(APPDIR)

if sys.platform == 'win32':
    APPDIR = os.path.join(os.environ['APPDATA'], APPNAME)
