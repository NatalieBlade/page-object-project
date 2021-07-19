from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        button = (self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET))
        button.click()

    def should_be_product_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT)

    def should_be_checked_name_in_basket(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name_on_page.text == product_name_in_basket.text, "Name is not correct"

    def should_be_price_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_ALERT)

    def should_be_correct_adding_product_price(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price_on_page.text == product_price_in_basket.text, "Prices are not equal"