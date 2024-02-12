import time
import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import random


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(random.randint(100000000, 999999999))
        register = LoginPage(browser, link)
        register.open()
        register.register_new_user(email, password)
        register.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_the_basket()
        # page.solve_quiz_and_get_code()
        page.check_added_product_name()
        page.check_added_product_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(), "Сообщение об успешном добавлении товара в корзину появляется при добавлении товара"


links_list = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail(reason="Этот тест ожидаемо проваливается")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.parametrize("links", links_list)
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code()
    page.check_added_product_name()
    page.check_added_product_price()


link_for_negative_tests = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_negative_tests)
    page.open()
    page.add_product_to_the_basket()
    assert page.is_not_element_present(), "Сообщение об успешном добавлении товара в корзину появилось"


@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_for_negative_tests)
    page.open()
    assert page.is_not_element_present(), "Сообщение об успешном добавлении товара в корзину появляется при добавлении товара"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_negative_tests)
    page.open()
    page.add_product_to_the_basket()
    assert page.is_disappeared(), "Сообщение о добавлении товара не исчезает"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_the_basket()
    page.basket_should_be_empty()
    assert page.should_be_message_that_the_basket_is_empty(), "Корзина, открытая со страницы продукта, не является пустой"