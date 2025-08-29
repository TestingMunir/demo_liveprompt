import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pageobjects.login_page import Login_page
from Utilities.BaseClass import BaseClass


import inspect


class Test_dashboard_page(BaseClass):


    def test_1login_invalid_username(self):
        log = self.getLogger()
        login_page = Login_page(self.driver)
        login_page.getusername().send_keys("munir.1admin@gmail.com")

        log.info("****** test_login_invalid_username started ******")
        log.info("user name is munir")
        assert "Invalid Credentials" == "test"
        """log.info("password  is Test123@")
        login_page.getpassword().send_keys("Test123@")
        login_page.getlogin().click()
        login_invalid_cred = login_page.driver.find_element(*Login_page.Login_invalid_credentials)
        if login_invalid_cred.text == "":
            login_invalid_cred = login_page.getinvalidCredentials_popup(2)
        log.info(type(login_invalid_cred))
        log.info(type(login_invalid_cred.text))
        log.info(str(login_invalid_cred.text))
        assert "Invalid Credentials" == str(login_invalid_cred.text)
        login_page.driver.refresh()
        log.info(" ******* test_login_invalid_username ended *******")"""


    def test_2login_invalid_password(self):
        log = self.getLogger()
        login_page = Login_page(self.driver)
        login_page.getusername().send_keys("munir.validadmin@gmail.com")

        log.info("****** test_login_invalid_username started ******")
        log.info("user name is munir")
        assert "Invalid Credentials" == "test"