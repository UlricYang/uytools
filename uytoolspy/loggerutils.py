import os

import loguru

from uytools import timeutils


class MyLogger(object):
    def __init__(self, *args, **kwargs):
        self.basedir = kwargs.get("basedir")
        self.logger = loguru.logger

    def getLogger(self):
        return self.logger

    def addFile(self, logpath=str()):
        if logpath:
            logdir = os.path.dirname(logpath)
            os.path.exists(logdir) or os.makedirs(logdir)
        if self.basedir:
            not os.path.exists(self.basedir) and os.makedirs(os.path.join(self.basedir, "logs"))
            self.logger.add(os.path.join(self.basedir, "logs", "{}.log".format(timeutils.now14())))
        return self
