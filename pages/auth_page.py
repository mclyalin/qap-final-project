from pages.base_page import BasePage
from pages.locators import AuthPageLocators
from settings import Settings


class AuthPage(BasePage):

    def __init__(self, web_driver):
        url = Settings.auth_page_url
        super().__init__(web_driver, url)

        self.right_section = self.find_element(AuthPageLocators.right_section)
        self.left_section = self.find_element(AuthPageLocators.left_section)
