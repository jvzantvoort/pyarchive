#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pyarchive.main.move.py - Class for pyarchive.main.move


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
from pyarchive.move import Move as PyArchiveAction
from pyarchive.main.common import Main

__author__ = "John van Zantvoort"
__copyright__ = "JDC"
__email__ = "john@vanzantvoort.org"
__license__ = "MIT"
__version__ = "1.0.1"

log = logging.getLogger('pyarchive.main')

class Move(Main):
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
        super(Move, self).__init__(**kwargs)
        self._act = PyArchiveAction()
        if self.noexec:
            self._act.noexec = True

    def main(self):
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

        Example::

          lala

        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """
        log.info("start")
        targets = list()
        if isinstance(self.srcfile, list):
            targets = self.srcfile
        else:
            targets = [self.srcfile]

        for target in targets:
            idf = self.identfile(target)

            log.debug(">> target: %s" % target)
            log.debug(">> id: %s" % idf)

            self._act(target, idf)

