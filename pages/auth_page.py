from pages.base_page import BasePage
from pages.locators import AuthLocators
from settings import Settings


class AuthPage(BasePage):

    def __init__(self, web_driver):
        url = Settings.auth_page_url
        super().__init__(web_driver, url)

        self.page_right = self.find_element(AuthLocators.page_right)
        self.page_left = self.find_element(AuthLocators.page_left)
