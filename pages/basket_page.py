from .base_page import BasePage
from selenium.webdriver.common.by import By
#from .locators import LoginPageLocators

class BasketPage(BasePage):
    def empty_basket(self):
        self.basket_is_empty()
        self.text_message_that_basket_is_empty()

    def basket_is_empty(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "#basket_formset > div > div"), "Basket is not empty!"

    def text_message_that_basket_is_empty(self):
        basket_text = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > p")
        a = basket_text.text
        basket_text2 = self.browser.find_element(By.XPATH, "//p")
        b = basket_text2.text
        assert a == b, 'Incorrect message!'
