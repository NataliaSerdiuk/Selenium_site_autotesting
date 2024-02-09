from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators, BasketPageLocator


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на логин не представлена"

    def go_to_the_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocator.BASKET_BUTTON)
        basket_button.click()
