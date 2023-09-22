import pytest
import inspect
import logging


@pytest.mark.usefixtures("setup")
class Invokation:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logging.basicConfig(encoding="utf-8")
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


# -------------------anohter format for logging ------------------------------------

# logger = logging.getLogger()
# if logger.hasHandlers():
#     logger.handlers.clear()
# logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)", datefmt='%d/%m/%Y %I:%M:%S %p')
# filehandler = logging.FileHandler('logFile.log')
# formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
#                       datefmt='%d/%m/%Y %I:%M:%S %p')
# filehandler.setFormatter(formatter)
# logger.addHandler(filehandler)
# logger.setLevel(logging.INFO)
# return logger
