import time
import re

from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoAlertPresentException
import math
import time

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
            time.sleep(300)
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME)
        product_name_added = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_ADDED)
        product_name_text = re.search(r'\b[a-zA-Z].*?[a-zA-Z]\b', product_name.text).group(0)
        product_name_added_text = re.search(r'\b[a-zA-Z].*?[a-zA-Z]\b', product_name_added.text).group(0)
        assert product_name_text == product_name_added_text,\
            f"Название книги в корзине {product_name_added_text} не соответствует названию выбранной книги {product_name_text}"

    def check_added_product_price(self):
        time.sleep(5)
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE)
        product_price_added = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE_ADDED)
        assert product_price.text == product_price_added.text,\
            f"Стоимость книги в корзине {product_price_added.text} не соответствует стоимости выбранной книги{product_price.text}"