from .base_page import BasePage
from .locators import DeliveryPageLocators

class DeliveryPage(BasePage):
    def should_be_empty_phone_form(self):
        if self.is_element_present(*DeliveryPageLocators.DELIV_FORM) == True:
            phone = self.browser.find_element(*DeliveryPageLocators.DELIV_PHONE).get_attribute('value')
            assert phone == "", \
                f"Phone has value {phone}, should be empty "


    def product_page_loaded(self):
        assert self.is_element_present(*DeliveryPageLocators.DELIV_FORM) == True, \
            f"Delivery page is not loaded, loaded page is {self.browser.current_url}" 