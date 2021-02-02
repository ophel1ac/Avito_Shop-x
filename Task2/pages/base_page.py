from .locators import BasePageLocators

from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait = timeout

    def open(self):
        self.browser.get(self.url)

    def login(self, email, password, timeout=6):
        if self.is_element_present(*BasePageLocators.LOG_FORM) == True:
            self.browser.find_element(*BasePageLocators.LOG_EMAIL).send_keys(email)
            self.browser.find_element(*BasePageLocators.LOG_PASS).send_keys(password)
            self.browser.find_element(*BasePageLocators.LOG_BUTTON).click()
   
    def is_element_present(self, how, what, timeout=6):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
