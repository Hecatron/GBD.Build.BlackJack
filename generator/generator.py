#! python3
"""
Script to generate the initial cmake wrapper class's
"""

import logging
from pygenerator.logwrapper import LogWrapper

# Setup logging
LogWrapper.LogLevel = logging.DEBUG
LogWrapper.setup()
log = LogWrapper.getlogger()

def main():
    try:
        print("test")
        raise IOError("test")

    # Output any errors
    except Exception as e:
        log.critical (e)
        if LogWrapper.LogLevel == logging.DEBUG:
            import traceback
            traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
	main()
