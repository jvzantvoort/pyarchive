#!/usr/bin/python

"""
Directory maintainer
"""

__author__ = "John van Zantvoort"
__version__ = "0.0.2"
__status__ = "Development"

# Import the libraries
# --------------------------------------
import re
from .config import ConfigByExtension


class ClassifyByExtension:

    def __init__(self):
        self.config = ConfigByExtension(autoload=True)
        self.patterns_reg = list()
        self.patterns_extra = [('Imgur', re.compile(r'.*\.Imgur\.zip$', re.I))]

    @staticmethod
    def mkset(pname, pitems):
        retv_y = re.compile('.*\\.(' + "|".join(pitems) + ')$', re.I)
        return pname, retv_y

    @property
    def patterns(self):
        if len(self.patterns_reg) == 0:
            for pname, pitems in self.config.patterns.iteritems():
                self.patterns_reg.append(self.mkset(pname, pitems))

        return self.patterns_reg

    def directories(self):
        retv = [x[0] for x in self.patterns]
        retv.append('Rest')
        retv.append('Imgur')
        return retv

    def identify(self, filepath):
        retv = 'Rest'

        for p_tuple in self.patterns:
            if p_tuple[1].match(filepath):
                retv = p_tuple[0]
                break

        for p_tuple in self.patterns_extra:
            if p_tuple[1].match(filepath):
                retv = p_tuple[0]
                break

        return retv

    def __call__(self, filepath):
        return self.identify(filepath)

    def info(self):
        retv = str()
        for row in self.patterns:
            retv += "\n" + row[0] + "\n"
            retv += row[1].pattern
        return retv

if __name__ == '__main__':

    cfe = ClassifyByExtension()
    print cfe('lala.jpg')
    print cfe('a.Imgur.zip')
    print cfe('lala.ziP')
