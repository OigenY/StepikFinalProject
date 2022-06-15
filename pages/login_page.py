from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "login is not presented in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        registration_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        registration_link.click()
        emailn = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        emailn.send_keys(email)
        first_field = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        first_field.send_keys("pSwfaLQ6hVA5Q8t")
        second_field = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        second_field.send_keys("pSwfaLQ6hVA5Q8t")
        button = self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        button.click()

