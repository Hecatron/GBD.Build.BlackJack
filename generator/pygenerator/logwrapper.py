"""
Coloured logging beween modules
"""

import logging, inspect
from colorlog import ColoredFormatter

# Wrapper class for logging
class LogWrapper(object):

    LogLevel = logging.DEBUG
    LogFormat = None
    LogStream = None

    @staticmethod
    def setup():
        #LogWrapper.LogFormat = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        LogWrapper.LogFormat = "%(log_color)s[%(asctime)s]:%(levelname)-7s:%(message)s"
        logging.root.setLevel(LogWrapper.LogLevel)
        formatter = ColoredFormatter(LogWrapper.LogFormat)
        LogWrapper.LogStream = logging.StreamHandler()
        LogWrapper.LogStream.setLevel(LogWrapper.LogLevel)
        LogWrapper.LogStream.setFormatter(formatter)

    @staticmethod
    def getlogger(modname = None):
        if modname == None:
            # Get Calling module name
            frm = inspect.stack()[1]
            modname = inspect.getmodule(frm[0]).__name__

        # Setup Logger
        log = logging.getLogger(modname)
        log.setLevel(LogWrapper.LogLevel)
        log.addHandler(LogWrapper.LogStream)
        return log

    @staticmethod
    def testoutput():
        log = LogWrapper.getlogger()
        log.debug("this is a debugging message")
        log.info("this is an informational message")
        log.warn("this is a warning message")
        log.error("this is an error message")
        log.fatal("this is a fatal message")
        log.critical("this is a critical message")
        return