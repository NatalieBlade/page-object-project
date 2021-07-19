from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner strong")
    PRODUCT_NAME_ON_PAGE = (By.TAG_NAME, "h1")
    PRODUCT_NAME_IN_BASKET = (By.CLASS_NAME, "alertinner")
    PRODUCT_PRICE_IN_BASKET_ALERT = (By.CSS_SELECTOR, "div:nth-child(2) > div > strong")
    PRODUCT_PRICE_ON_PAGE = (By.CLASS_NAME, "price_color")
    PRODUCT_PRICE_IN_BASKET = (By.TAG_NAME, "div > p:nth-child(1) > strong")