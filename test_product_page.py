# import time
#
# from .pages.product_page import PageObject
#
# def test_guest_can_add_product_to_basket(browser):
#     browser.implicitly_wait(10)
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     link2 = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = PageObject(browser, link2)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.add_to_basket()          # выполняем метод страницы — переходим на страницу логина
#     page.solve_quiz_and_get_code()
#     page.messages_check()
#     page.messages_check_second()
#     time.sleep(15)




import time

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.open_product_page()
    page.open_basket_page()
    product_page = BasketPage(browser, browser.current_url)
    product_page.empty_basket()
