
import logging, inspect
from colorlog import ColoredFormatter

class Logger(object):

    """
    Wrapper class for logging
    """

    LogLevel = logging.DEBUG
    LogFormat = None
    LogStream = None

    @staticmethod
    def setup():
        """Initial Global Setup of the Logger"""
        Logger.LogFormat = "%(log_color)s[%(asctime)s]:%(levelname)-7s:%(message)s"
        logging.root.setLevel(Logger.LogLevel)
        formatter = ColoredFormatter(Logger.LogFormat)
        Logger.LogStream = logging.StreamHandler()
        Logger.LogStream.setLevel(Logger.LogLevel)
        Logger.LogStream.setFormatter(formatter)

    @staticmethod
    def getlogger(modname = None):
        """Get the Logger instance for the current class"""
        if modname == None:
            # Get Calling module name
            frm = inspect.stack()[1]
            modname = inspect.getmodule(frm[0]).__name__

        # Setup Logger
        log = logging.getLogger(modname)
        log.setLevel(Logger.LogLevel)
        log.addHandler(Logger.LogStream)
        return log

    @staticmethod
    def testoutput():
        """Test the Logger"""
        log = Logger.getlogger()
        log.debug("this is a debugging message")
        log.info("this is an informational message")
        log.warn("this is a warning message")
        log.error("this is an error message")
        log.fatal("this is a fatal message")
        log.critical("this is a critical message")
        return
