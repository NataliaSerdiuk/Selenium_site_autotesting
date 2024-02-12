from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .base_page import BasePage
from .locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def basket_should_be_empty(self, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(BasketPageLocator.NOT_EMPTY_BASKET))
        except TimeoutException:
            return True
        return False

    def should_be_message_that_the_basket_is_empty(self, timeout=2):
        assert WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(BasketPageLocator.EMPTY_BASKET_MESSAGE)), "Корзина, открытая со страницы продукта, не является пустой"

