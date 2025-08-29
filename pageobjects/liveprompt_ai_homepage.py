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

    Login_username = (By.NAME, "username")
    Login_password = (By.NAME, "password")
    login_button = (By.XPATH, "//button/span[text()='Login']")
    Login_invalid_credentials = (By.XPATH, "//div[text()='Invalid Credentials']")
    Login_enter_pass = (By.XPATH, "//span[text()='Please enter password']")
    Login_enter_username = (By.XPATH, "//span[text()='Please enter valid username']")
    Login_forgot_password = (By.XPATH, "//a/article[text()='Forgot Password?']")
    Login_popup_yes_button="//div[@class='ant-modal-content']//span[text()='Yes']"
    Login_already_log_in_popup="//div[@class='Toastify']/div"
    # Locator for 'Enter Email for OTP Authentication' title
    Email_otp_auth_title = (By.XPATH, "//p[@class='title' and text()='Enter Email for OTP Authentication']")

    def getusername(self):
        return self.driver.find_element(*Login_page.Login_username)

    def getpassword(self):
        return self.driver.find_element(*Login_page.Login_password)

    def getlogin(self):
        return self.driver.find_element(*Login_page.login_button)

    def getinvalidCredentials_popup(self, seconds):
        self.wait = WebDriverWait(self.driver, seconds)
        # login_invalid_ele=self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Invalid Credentials']")))
        time.sleep(seconds)
        # return self.driver.find_element(*Login_page.Login_invalid_credentials)
        login_invalid_ele = self.driver.find_element(*Login_page.Login_invalid_credentials)
        return login_invalid_ele

    def get_empty_username_error(self):
        return self.driver.find_element(*Login_page.Login_enter_username)

    def get_empty_password_error(self):
        return self.driver.find_element(*Login_page.Login_enter_pass)

    def get_forgot_password(self):
        return self.driver.find_element(*Login_page.Login_forgot_password)

    def click_on_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        return actions.perform()

    def get_email_otp_auth_title(self):
        return self.driver.find_element(*Login_page.Email_otp_auth_title)

