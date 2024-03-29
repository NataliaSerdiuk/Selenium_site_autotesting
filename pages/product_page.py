import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import *


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


    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocator.PRESENT_ELEMENT), "Сообщение об успешном добавлении товара в корзину"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(ProductPageLocator.PRESENT_ELEMENT), "Сообщение о добавлении товара не исчезает"
