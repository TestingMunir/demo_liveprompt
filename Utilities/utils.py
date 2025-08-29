
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_visibility_of_element_located(driver, seconds,locator):
    wait = WebDriverWait(driver, seconds)
    ele = wait.until(
        EC.visibility_of_element_located(locator))
    return ele

'''def get_button(self, page_class, locator_name):
    # dynamically get locator tuple from the page class
    locator = getattr(page_class, locator_name)
    return self.driver.find_element(*locator)'''
def get_button(driver, locator):
    return driver.find_element(locator)

'''def get_element(self, page_class, locator_name):
    # dynamically get locator tuple from the page class
    locator = getattr(page_class, locator_name)
    return self.driver.find_element(*locator)'''


def get_element(driver,locator):
    return driver.find_element(locator)

from urllib.parse import urlparse

def get_env_from_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc  # e.g. www.liveprompt.ai or uat.liveprompt.ai
    first_part = host.split(".")[0]  # take only the first part
    return first_part