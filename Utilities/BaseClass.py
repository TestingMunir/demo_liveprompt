import inspect
import logging
import os

import pytest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#from pageObjects.Login_page import Login_page


@pytest.mark.usefixtures("setup")
class BaseClass:



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        #fileHandler = logging.FileHandler(str(current_time)+'logfile.log')
        # Create logs folder if it doesn't exist
        os.makedirs("logs", exist_ok=True)

        # Generate unique log file for this run
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = f"logs/logfile_{now}.log"

        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

