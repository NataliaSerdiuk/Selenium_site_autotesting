import pytest
from pages.main_page import MainPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_the_basket()
    page.basket_should_be_empty()
    assert page.should_be_message_that_the_basket_is_empty(), "Корзина, открытая с главной страницы, не является пустой"
