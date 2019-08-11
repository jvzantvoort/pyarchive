"""Exceptions for the pyarchive package"""

__author__ = "John van Zantvoort"
__email__ = "john@vanzantvoort.org"
__copyright__ = "John van Zantvoort"


class PyArchiveException(Exception):
    """
    :param message: the error message
    :returns: Formatted exception message
    """
    def __init__(self, message):
        self.message = message
        Exception.__init__(self)

    def __str__(self):
        return "PyArchive Error %s" % self.message

class PyArchiveConfigException(Exception):
    """
    :param message: the error message
    :returns: Formatted exception message
    """
    def __init__(self, message):
        self.message = message
        Exception.__init__(self)

    def __str__(self):
        return "PyArchive Config Error %s" % self.message
