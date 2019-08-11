
import os.path
import pyarchive.config
import shutil
import logging


class Move(object):
    """move targets to their respective destination

    move targets from source to destination. If the destination exists a
    duplicates directory is inserted with an incremental number. If the path
    with the number exists the number is incremented.

    Example::

      from pyarchive.move import Move
      mover = Move()
      mover.movefile("/tmp/foo.jpg", "~/Archive/Images")

    """

    def __init__(self):
        self.config = pyarchive.config.ConfigMain(autoload=True)
        self.logger = logging.getLogger('pyarchive.move')

    def makedir(self, dirname):
        """fancy create directory

        :param dirname: name of the directory
        :type dirname: str
        :returns: absolute path of the directory
        :rtype: str
        """

        if not os.path.isabs(dirname):
            dirname = os.path.join(self.config.archive_dir, dirname)

        dirname = os.path.realpath(dirname)

        if os.path.isdir(dirname):
            self.logger.debug("path %s exists" % dirname)
            return dirname

        try:
            os.makedirs(dirname)

        except OSError as oerr:
            self.logger.error(str(oerr))

        return dirname

    def movedup(self, srcfile, destdir):
        """move duplicates

        :param srcfile: the source file
        :param destdir: the destdir
        :type srcfile: str
        :type destdir: str
        """
        basename = os.path.basename(srcfile)
        count = 1
        newdir = None

        while True:
            newdir = os.path.join(destdir, self.config.dupfmt % count)
            count = count + 1

            if not os.path.exists(newdir):
                break

            if not os.path.exists(os.path.join(newdir, basename)):
                break

        newdir = self.makedir(newdir)
        dstfile = os.path.join(newdir, basename)

        self.logger.info("move {0} {1}".format(srcfile, dstfile))
        shutil.move(srcfile, dstfile)

    def movefile(self, srcfile, destdir):
        """move files

        :param srcfile: the source file
        :param destdir: the destdir
        :type srcfile: str
        :type destdir: str
        """
        self.logger.info("in {0}".format(srcfile))

        basename = os.path.basename(srcfile)
        destdir = self.makedir(destdir)
        dstfile = os.path.join(destdir, basename)

        if not os.path.exists(dstfile):
            self.logger.info("move {0} {1}".format(srcfile, dstfile))
            shutil.move(srcfile, dstfile)
            return

        self.movedup(srcfile, destdir)

    def __call__(self, srcfile, destdir):
        self.movefile(srcfile, destdir)

