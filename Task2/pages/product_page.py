from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def choose_item(self):
        self.browser.find_elements(*ProductPageLocators.CHOOSE_PRODUCT)[0].click()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def add_to_delivery(self):
        self.browser.find_element(*ProductPageLocators.ORDER_BUTTON).click()

    def product_page_loaded(self):
        self.is_element_present(*ProductPageLocators.ORDER_BUTTON)
    
