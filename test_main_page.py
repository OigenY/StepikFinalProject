import time
import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
@pytest.mark.mainpage
class TestMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        #link2 = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(8)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        time.sleep(8)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.open_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.empty_basket()
        time.sleep(8)
