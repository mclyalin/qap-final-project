import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from settings import Settings


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or Settings.auth_page_url

        super().__init__(web_driver, url)

    right_section = WebElement(id='page-right')
    left_section = WebElement(id='page-left')

    form = WebElement(css_selector='.login-form-container form.login-form')
    form_title = WebElement(css_selector='.login-form-container h1')
    auth_type_menu = WebElement(css_selector='form.login-form .tabs-input-container__tabs')
    input_username = WebElement(id='username')
    input_password = WebElement(id='password')
    submit_button = WebElement(id='kc-login')

    forgot_password_link = WebElement(id='forgot_password')
    register_link = WebElement(id='kc-register')

    auth_type_menu_tabs = ManyWebElements(xpath='//div[contains(@class,"tabs-input-container__tabs")]/child::*')
    phone_tab = WebElement(id='t-btn-tab-phone')
    email_tab = WebElement(id='t-btn-tab-mail')
    login_tab = WebElement(id='t-btn-tab-login')
    ls_tab = WebElement(id='t-btn-tab-ls')

    input_username_placeholder = WebElement(xpath='//*[@id="username"]/following-sibling::*[contains(@class,"placeholder")]')
