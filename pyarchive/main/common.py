#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pyarchive.main.common.py - Class for pyarchive.main.common


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
import logging
from pyarchive.identify import ClassifyByExtension

__author__ = "John van Zantvoort"
__copyright__ = "JDC"
__email__ = "john@vanzantvoort.org"
__license__ = "MIT"
__version__ = "1.0.1"

log = logging.getLogger('pyarchive.main')

class Main(object):
    """brief explanation

    extended explanation

    :param arg1: description
    :param arg2: description
    :type arg1: type description
    :type arg1: type description
    :return: return description
    :rtype: the return type description

    Example::

      obj = Class()

    .. seealso:: blabla
    .. warnings also:: blabla
    .. note:: blabla
    .. todo:: blabla
    """

    def __init__(self, **kwargs):
        self._identfile = ClassifyByExtension()

        self.pyarchive_location = kwargs.get('pyarchive_location')
        self.srcfile = kwargs.get('srcfile')
        self.noexec = kwargs.get('noexec')

    def identfile(self, target):
        """short description

        extended description

        :param arg1: the first value
        :param arg2: the first value
        :param arg3: the first value
        :type arg1: int, float,...
        :type arg2: int, float,...
        :type arg3: int, float,...
        :returns: arg1/arg2 +arg3
        :rtype: int, float
        """
        return os.path.join(self.pyarchive_location, self._identfile(target))
