from selenium.webdriver.common.by import By
    

class BasePageLocators:
    LOG_FORM = (By.CSS_SELECTOR, '.auth-app-login-form-2_SQa')
    LOG_EMAIL = (By.CSS_SELECTOR, '.input-input-25uCh[name="login"]')
    LOG_PASS = (By.CSS_SELECTOR, '.input-input-25uCh[name="password"]')
    LOG_BUTTON = (By.CSS_SELECTOR, '.button-button-2Fo5k[name="submit"]')

class ProductPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, '.item-buyer-button-1-zak')
    CHOOSE_PRODUCT = (By.CSS_SELECTOR, '.link-link-39EVK[data-marker="item-title"]')


class DeliveryPageLocators:
    DELIV_FORM = (By.CSS_SELECTOR, '#js-order-widget')
    DELIV_PHONE = (By.CSS_SELECTOR, '.input-input-1q3_6[name="phone"]')