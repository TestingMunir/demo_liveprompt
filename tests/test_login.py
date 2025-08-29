import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Utilities.XLPANA import pd_get_file
from Utilities.utils import wait_visibility_of_element_located, get_env_from_url
from pageobjects.login_page import Login_page
from Utilities.BaseClass import BaseClass


import inspect

@pytest.mark.usefixtures("setup", "env_name")
class Test_Login_page(BaseClass):
    """
    testing basic login functionalities
    """

    def setup_method(self, method):
        # Get env from pytest config
        self.log = self.getLogger()
        pass

    #helper method to ensure at start of each test driver is on homepage
    @pytest.mark.usefixtures("env_name")
    def go_to_login_page(self):
        login_page = Login_page(self.driver)
        try:
            log_out = login_page.wait_visibility_of_element_located(
            seconds=2,
            locator=Login_page.log_out)
            log_out.click()
            try:
                login_page.get_button(Login_page.signout).click()
            except:
                signout = login_page.wait_visibility_of_element_located(
                    seconds=2,
                    locator=Login_page.home_page_verification_text)
                signout.click()
        except:
            current_url = login_page.driver.current_url
            print(current_url)
            env_name=get_env_from_url(current_url)
            if env_name == "www":
                login_page.driver.get("https://www.liveprompt.ai/")
            elif env_name == "uat":
                Login_page.driver.get("https://uat.liveprompt.ai/")

            elif env_name == "dev":
                login_page.driver.get("https://dev.liveprompt.ai/")

        finally:
            # precondition homepage

            gethome_page_verification_text = login_page.wait_visibility_of_element_located(
            seconds=2,
            locator=Login_page.home_page_verification_text).text
            self.log.info("home page verification text is  %s", gethome_page_verification_text)
            if gethome_page_verification_text == "Your AI Copilot for":
                self.log.info("****** precondition passed******")

    def test_signup(self, ):
        self.log.info("****** test_sign_up******")
        login_page = Login_page(self.driver)
        try:
            # precondition homepage
            gethome_page_verification_text = login_page.wait_visibility_of_element_located(
                seconds=2,
                locator=Login_page.home_page_verification_text).text
            self.log.info("****** test_sign_up******")
            self.log.info("home page verification text is  %s", gethome_page_verification_text)
            if gethome_page_verification_text == "Your AI Copilot for":
                self.log.info("****** precondition passed******")


        except:
            self.go_to_login_page()
        finally:

            # test logic
            login_page.get_element(Login_page.sign_up_button).click()
            create_account_header_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                      locator=Login_page.create_account_header)
            create_account_header_text = create_account_header_ele.text
            self.log.info("create_account_header_text  is  %s", create_account_header_text)
            data = pd_get_file("./Testdata/signup_users.xlsx")
            login_page.get_element(Login_page.agree_terms).click()
            login_page.get_element(Login_page.sign_up_with_email).click()
            create_account_header_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                      locator=Login_page.create_account_header)
            create_account_header_text = create_account_header_ele.text
            self.log.info("create_account_header_text  is  %s", create_account_header_text)
            login_page.get_element(Login_page.fullname).send_keys(data["Fullname"][1])
            login_page.get_element(Login_page.email).send_keys(data["Email"][1])
            login_page.get_element(Login_page.password).send_keys(data["Passwords"][1])
            login_page.get_element(Login_page.confirm_password).send_keys(data["Confirm Password"][1])
            self.log.info(
                "fullname: %s | email: %s | password: %s | confirm password: %s",
                data["Fullname"][1],
                data["Email"][1],
                data["Passwords"][1], data["Confirm Password"][1]
            )

            login_page.get_element(Login_page.create_account).click()
            confirm_your_account_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                     locator=Login_page.confirm_your_account)
            self.log.info("confirm_your_account_ele_text  is  %s", confirm_your_account_ele.text)
            # assertion
            assert confirm_your_account_ele.text == "Check your email to confirm your account"

    def test_login(self):
        self.log.info("****** test_sign_up******")
        login_page = Login_page(self.driver)
        # precondition homepage
        try:
            gethome_page_verification_text = login_page.wait_visibility_of_element_located(
                seconds=2,
                locator=Login_page.home_page_verification_text).text
            self.log.info("****** test_sign_up******")
            self.log.info("home page verification text is  %s", gethome_page_verification_text)
            if gethome_page_verification_text == "Your AI Copilot for":
                self.log.info("****** precondition passed******")

        except:
            self.go_to_login_page()

        finally:

            # test logic
            login_page.get_element(login_page.log_in).click()
            log_in_page_header_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                   locator=(
                                                                                       Login_page.log_in_page_header))
            log_in_page_header_text = log_in_page_header_ele.text
            self.log.info("log_in_page_header_text  is  %s", log_in_page_header_text)
            data = pd_get_file("./TestData/login_creds.xlsx")
            login_page.get_button(Login_page.sign_in_with_email).click()
            login_page.get_button(Login_page.email).send_keys(data["Email"][1])
            login_page.get_button(Login_page.password).send_keys(data["Passwords"][1])
            self.log.info(
                " email: %s | password: %s ",
                data["Email"][1],
                data["Passwords"][1],
            )
            sign_in_button = login_page.driver.find_element(*Login_page.sign_in)

            # Scroll until the element is visible
            login_page.driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)
            sign_in_button.click()
            join_meeting_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                     locator=Login_page.join_meeting)

            # assertion
            self.log.info("join_meeting_ele.text is  %s", join_meeting_ele.text)
            assert join_meeting_ele.text == "Join Meeting"


    def test_invalid_creds(self):
        self.log.info("****** test_invalid_creds ******")
        login_page = Login_page(self.driver)
        # precondition homepage
        try:
            gethome_page_verification_text = login_page.wait_visibility_of_element_located(
                seconds=2,
                locator=Login_page.home_page_verification_text).text
            self.log.info("****** test_sign_up******")
            self.log.info("home page verification text is  %s", gethome_page_verification_text)
            if gethome_page_verification_text == "Your AI Copilot for":
                self.log.info("****** precondition passed******")

        except:
            self.go_to_login_page()

        finally:
            self.log.info("****** Test logic started ******")
            # test logic
            login_page.get_element(login_page.log_in).click()
            log_in_page_header_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                   locator=(
                                                                                       Login_page.log_in_page_header))
            log_in_page_header_text = log_in_page_header_ele.text
            self.log.info("log_in_page_header_text  is  %s", log_in_page_header_text)
            data = pd_get_file("./TestData/login_creds.xlsx")
            login_page.get_button(Login_page.sign_in_with_email).click()
            login_page.get_button(Login_page.email).send_keys(data["Email"][2])
            login_page.get_button(Login_page.password).send_keys(data["Passwords"][2])
            self.log.info(
                " email: %s | password: %s ",
                data["Email"][2],
                data["Passwords"][2],
            )
            sign_in_button = login_page.driver.find_element(*Login_page.sign_in)

            # Scroll until the element is visible
            login_page.driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)
            sign_in_button.click()
            invalid_cred_meassage_ele = login_page.wait_visibility_of_element_located(seconds=5,
                                                                                     locator=Login_page.invalid_cred_meassage)

            # assertion
            self.log.info("invalid_cred_meassage_ele.text is  %s", invalid_cred_meassage_ele.text)
            assert invalid_cred_meassage_ele.text == "Invalid login credentials"


