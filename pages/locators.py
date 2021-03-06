from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_TO_REGISTER = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner strong")
    PRODUCT_NAME_ON_PAGE = (By.TAG_NAME, "h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE_IN_BASKET_ALERT = (By.CSS_SELECTOR, "div:nth-child(2) > div > strong")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

class BasketLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    DISAPPEARENCE_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    NO_ITEMS_IN_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")