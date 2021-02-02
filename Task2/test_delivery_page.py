import pytest

from .pages.delivery_page import DeliveryPage
from .pages.product_page import ProductPage



def test_phone_is_empty(browser):
    log_email = ""
    log_password = ""
    # Ссылка на поисковую выдачу товаров, но попадаются товары без кнопки доставки и тест падает
    product_link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"

    # Ссыслка на товар, с кнопкой доставки, в этом случае нужно отключить choose_item()
    # product_link = "https://www.avito.ru/sochi/odezhda_obuv_aksessuary/kostyum_muzhskoy_2084663797"
    page = ProductPage(browser, product_link)
    page.open()
    # Выбирает первый товар из поиска и переключается на новую вкладку
    page.choose_item()
    page.add_to_delivery()

    # Логин может упасть из-за капчи
    page.login(log_email, log_password)

    delivery_page = DeliveryPage(browser, browser.current_url)
    delivery_page.should_be_empty_phone_form()
    
    