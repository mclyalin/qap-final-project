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

    left_section = WebElement(id='page-left')
    form = WebElement(css_selector='.register-form-container form.register-form')
    form_title = WebElement(css_selector='.register-form-container h1')
    input_first_name = WebElement(css_selector='input[name="firstName"]')
    input_last_name = WebElement(css_selector='input[name="lastName"]')
    select_region = WebElement(xpath='//div[contains(@class,"register-form__dropdown")]//input')
    input_email_phone = WebElement(id='address')
    input_password = WebElement(id='password')
    password_confirm = WebElement(id='password-confirm')
    submit_button = WebElement(xpath='//button[contains(@class,"register-form__reg-btn")]')
    policy_agreement_link = WebElement(css_selector='.auth-policy a')
