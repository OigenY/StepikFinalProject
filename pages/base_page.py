from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        #инициализация работы экземпляра драйвера, юрлы, время ожидания

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    #проверка что элемент присутствует

    def open(self):
        self.browser.get(self.url)
        #экземпляр открывания юрлы

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    # is_not_element_present - используется для проверки того что элемент не появляется на странице в течении заданого вермени (если элемент появляется - то тест падает)
    #пример реализации
    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # пример реализации тот же
    # is_disappeared - проверка того, что элемент исчезает в течении заданого времени
    def open_basket_page(self):
        basket_page = self.browser.find_element(By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
        basket_page.click()
    # открывание корзины
    def open_product_page(self):
        all_products_page = self.browser.find_element(By.CSS_SELECTOR, "#browse > li > ul > li:nth-child(1) > a")
        all_products_page.click()
        product_page = self.browser.find_element(By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(1) > article > div.image_container > a > img")
        product_page.click()


    # открывание страницы с товаром




