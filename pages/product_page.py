from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
import math
from selenium.webdriver.common.by import By
class PageObject(BasePage):
    def add_to_basket(self):
        butt1 = self.browser.find_element(By.CLASS_NAME, "add-to-basket")
        butt1.click()

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
        except NoAlertPresentException:
            print("No second alert presented")

    def messages_check(self):
        book_name = self.browser.find_element(By.TAG_NAME, "h1")
        a = book_name.text
        book_name_in_basket = self.browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
        b = book_name_in_basket.text
        assert a == b, 'Название товара не совпадает'

    def messages_check_second(self):
        price_name = self.browser.find_element(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
        c = price_name.text
        price_name_in_basket = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
        d = price_name_in_basket.text
        assert c == d, 'Название товара не совпадает'
