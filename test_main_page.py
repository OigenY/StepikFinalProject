#import time


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
    #time.sleep(10)




# import time
#
# from .pages.main_page import MainPage
# from .pages.basket_page import BasketPage
# #from .pages.login_page import LoginPage

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     #link2 = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     page.should_be_login_link()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#     time.sleep(10)



import time

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
#from .pages.login_page import LoginPage
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.open_basket_page()
    #ime.sleep(10)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket()
