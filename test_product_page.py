import time
from pages.base_page import BasePage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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
