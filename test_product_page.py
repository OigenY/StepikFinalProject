
#Есть вероятность, что какой-то тест упадет, потому что будет 500 ошибка сервера.

import time
import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
#@pytest.mark.productpage
#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
class TestProductPage():
    #@pytest.mark.parametrize('link', urls)
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link2 = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.messages_check()
        page.messages_check_second()
        time.sleep(8)

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.open_product_page()
        page.open_basket_page()
        product_page = BasketPage(browser, browser.current_url)
        product_page.empty_basket()
        time.sleep(8)

    def test_guest_should_see_login_link_on_product_page(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        time.sleep(8)

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(8)

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.success_message_is_not_element_present()
        time.sleep(8)

    def test_guest_cant_see_success_message(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.success_message_is_not_element_present()
        time.sleep(8)

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.success_message_is_disappeared()
        time.sleep(8)

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        # link2 = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
        time.sleep(8)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link2 = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.messages_check()
        page.messages_check_second()
        time.sleep(8)

    def test_user_cant_see_success_message(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.success_message_is_not_element_present()
        time.sleep(8)
