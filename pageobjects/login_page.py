from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pageObjects.CheckoutPage import CheckOutPage
import time

class Login_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = None


    home_page_verification_text=(By.XPATH,"//span[text()='Your AI Copilot for ']")
    sign_up_button=(By.XPATH,"//button[text()='Sign up']")
    fullname=(By.ID,"fullName")
    email=(By.ID,"email")
    password=(By.ID,"password")
    confirm_password=(By.ID,"confirmPassword")
    create_account=(By.XPATH,"//button[contains(.,'Create account')]")
    create_account_header=(By.XPATH,"//h1[text()='Create your account']")
    agree_terms=(By.XPATH,"//input[@id='agree-terms']")
    sign_up_with_email=(By.XPATH,"//*[text()='Sign up with email']")
    confirm_your_account=(By.XPATH,"//*[text()='Check your email to confirm your account']")

    #Log in page
    log_in=(By.XPATH,"//button[text()='Log in']")
    log_in_page_header=(By.XPATH,"//*[text()='Sign in to your account to continue']")
    sign_in_with_email=(By.XPATH,"//*[text()='Sign in with email']")
    sign_in=(By.XPATH,"//button[text()='Sign in']")
    join_meeting=(By.XPATH, "//span[contains(text(),'Join Meeting')]")
    invalid_cred_meassage=(By.XPATH,"//div[contains(text(),'Invalid login credentials')]")

    #log_out
    log_out=(By.XPATH,"//button/div/p[contains(.,'Rm')]")
    signout=(By.XPATH, "//button[.='Sign Out']")




    '''def getsign_up_button(self):
        return self.driver.find_element(*Login_page.sign_up_button)

    def getfullname(self):
        return self.driver.find_element(*Login_page.fullname)

    def getemail(self):
        return self.driver.find_element(*Login_page.email)

    def getpassword(self):
        return self.driver.find_element(*Login_page.password)

    def getconfirm_password(self):
        return self.driver.find_element(*Login_page.confirm_password)

    def gethome_page_verification_text(self, seconds):
        self.wait = WebDriverWait(self.driver, seconds)
        home_page_verification_text_ele=self.wait.until(EC.visibility_of_element_located(Login_page.home_page_verification_text))
        return home_page_verification_text_ele

    def get_create_account_button(self):
        return self.driver.find_element(*Login_page.create_account)
    def get_agree_terms(self):
        return self.driver.find_element(*Login_page.agree_terms)
    def get_Sign_up_with_email_button(self):
        return self.driver.find_element(*Login_page.Sign_up_with_email)

    def getlog_in_button(self):
        return self.driver.find_element(*Login_page.log_in)'''

    #############_____________#############
    def get_button(self,locator):
        return self.driver.find_element(*locator)

    def get_element(self,locator):
        return self.driver.find_element(*locator)

    def wait_visibility_of_element_located(self,seconds,locator):
        wait = WebDriverWait(self.driver, seconds)
        ele = wait.until(
            EC.visibility_of_element_located(locator))
        return ele









    def click_on_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        return actions.perform()



