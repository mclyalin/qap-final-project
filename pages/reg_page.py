import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from pages.auth_page import AuthPage
from settings import Settings


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or Settings.base_url

        super().__init__(web_driver, url)

    def open(self):
        self.open_link.click()

    open_link = AuthPage.register_link
