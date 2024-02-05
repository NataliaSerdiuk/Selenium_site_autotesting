from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocator():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_ADDED =  (By.CSS_SELECTOR, ".alertinner p strong")
