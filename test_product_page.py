import time
from pages.base_page import BasePage
from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()

    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    time.sleep(5)

    product_page = ProductPage(browser, link)
    product_page.should_be_product_in_basket_message()
    product_page.should_be_checked_name_in_basket()
    product_page.should_be_correct_adding_product_price()
    product_page.should_be_price_in_basket_message()
