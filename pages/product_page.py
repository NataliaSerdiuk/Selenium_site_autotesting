import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import math


class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        link = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME)
        product_name_added = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_ADDED)
        assert product_name.text == product_name_added.text, \
            f"Название книги в корзине '{product_name_added.text}' не соответствует названию выбранной книги '{product_name.text}'"

    def check_added_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE)
        product_price_added = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE_ADDED)
        assert product_price.text == product_price_added.text, \
            f"Стоимость книги в корзине ({product_price_added.text}) не соответствует стоимости выбранной книги ({product_price.text})"

    def is_not_element_present(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(ProductPageLocator.PRESENT_ELEMENT))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(ProductPageLocator.PRESENT_ELEMENT))
        except TimeoutException:
            return False
        return True
