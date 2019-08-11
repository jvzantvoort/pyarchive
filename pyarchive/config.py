"""
Handle config objects

"""

import os
import yaml
from .constants import APPDIR

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config(object):
    """Base object for configuration

    """

    def __init__(self, **kwargs):
        if not os.path.isdir(APPDIR):
            os.makedirs(APPDIR)

        self.config_data = dict()
        self.configfile = str()
        self.configname = kwargs.get('config_name', 'undefined')

        self.configfile = os.path.join(APPDIR, self.configname + ".yml")

        self.configfile = kwargs.get('configfile', self.configfile)

        autoload = kwargs.get('autoload', False)

        if autoload:
            self.load()

    def defaults(self):
        return {}

    def load(self):
        try:
            with open(self.configfile) as stream:
                self.config_data = load(stream, Loader=Loader)

        except IOError:
            self.config_data = self.defaults
            self.write()

    def write(self):
        data = dump(self.config_data, Dumper=Dumper, explicit_start=True,
                    default_flow_style=False)
        ofh = open(self.configfile, 'w')
        ofh.write(data)
        ofh.close()


class ConfigMain(Config):
    """Main config for the application"""

    def __init__(self, **kwargs):
        kwargs['config_name'] = "main"
        super(ConfigMain, self).__init__(**kwargs)

    @property
    def defaults(self):
        retv = dict()
        retv['archive_dir'] = os.path.expanduser('~/Archive')
        retv['dupfmt'] = "duplicate%03d"
        return retv

    @property
    def dupfmt(self):
        return self.config_data.get('dupfmt')

    @property
    def archive_dir(self):
        return self.config_data.get('archive_dir')

class ConfigByExtension(Config):
    """

    Example::

        cfg = ConfigByExtension(autoload=True)
        cfg.load()
    """

    def __init__(self, **kwargs):
        kwargs['config_name'] = "extensions"
        super(ConfigByExtension, self).__init__(**kwargs)

    @property
    def patterns(self):
        return self.config_data

    @property
    def defaults(self):
        retv = {'Compressed': ['zip', 'xz', 'gz', 'tgz', 'bz2', 'rar', 'tar'],
                'Contacts': ['contact', 'vcf'],
                'Database': ['sql'],
                'DiskImages': ['img', 'iso'],
                'Documents': ['tex',
                              'doc',
                              'docx',
                              'pdf',
                              'xls',
                              'pdf',
                              'asd',
                              'ods',
                              'ott',
                              'odt',
                              'xps',
                              'htm',
                              'html',
                              'gdoc',
                              'gsheet'],
                'DownloadFiles': ['nzb', 'torrent'],
                'GoogleEarth': ['kmz'],
                'Images': ['jpg', 'jpe', 'jpeg', 'png', 'bmp', 'gif'],
                'Keys': ['ppk', 'der', 'pem'],
                'Movies': ['mkv', 'avi', 'mpg', 'mpeg', 'asf', 'mov', 'wmv',
                           'flv'],
                'Music': ['mp3', 'ogg'],
                'Software': ['pkg', 'dmg', 'rpm', 'exe', 'msi'],
                'Source': ['c', 'cpp', 'pl', 'pm', 'py', 'h', 'sh', 'cmd',
                           'bat', 'class', 'jnlp', 'php']}
        return retv
