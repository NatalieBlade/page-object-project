from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "'login' is absent in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form")
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is absent"
        assert True

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(
            email)
        password = f.password()
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
            password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_TO_REGISTER).click()