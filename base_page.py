from selenium.common.exceptions import NoSuchElementException
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

    def open(self):
        self.browser.get(self.url)
        #экземпляр открывания юрлы