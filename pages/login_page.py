from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login отсутствует в текущем Url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Форма ввода логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Форма регистрации отсутствует"

    def register_new_user(self, email, password):
        register_email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        enter_email = register_email_field.send_keys(email)
        register_password_field_1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        enter_password_1 = register_password_field_1.send_keys(password)
        register_password_field_2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        enter_password_2 = register_password_field_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
