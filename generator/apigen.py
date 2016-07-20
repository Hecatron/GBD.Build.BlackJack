#!python3
"""
Script to generate the initial cmake wrapper class's / API
"""

import logging, sys
from apigen.Logger import Logger
from apigen.Generator import Generator

# Setup logging
Logger.LogLevel = logging.DEBUG
Logger.setup()
log = Logger.getlogger()

def main():
    try:
        # Generate Low level API Bindings
        gen = Generator()
        gen.Generate()

    # Output any errors
    except Exception as e:
        log.critical (e)
        if Logger.LogLevel == logging.DEBUG:
            import traceback
            traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
	main()
