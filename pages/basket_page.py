from pages.base_page import BasePage
from pages.locators import BasketLocators

class BasketPage(BasePage):

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.ITEMS_IN_BASKET)

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketLocators.NO_ITEMS_IN_BASKET_TEXT)