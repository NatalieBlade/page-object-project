from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        button = (self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET))
        button.click()

    def should_be_product_in_basket_message(self):
        adding_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT)
        assert adding_message.text == "The shellcoder's handbook", "Message is not found"

    def should_be_checked_name_in_basket(self):
        product_name_on_page = self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        product_name_in_basket = self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name_on_page == product_name_in_basket, "Name is not correct"

    def should_be_price_in_basket_message(self):
        price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_ALERT)
        assert price_message.text == "Deferred benefit offer", "No price alert in the basket"

    def should_be_correct_adding_product_price(self):
        product_price_on_page = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        product_price_in_basket = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price_on_page == product_price_in_basket, "Prices are not equal"