import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from settings import Settings


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or Settings.base_url

        super().__init__(web_driver, url)

    def sign_in(self, login, password):
        self.input_username.send_keys(login)
        self.input_password.send_keys(password)
        if self.remember_me_checkbox.get_attribute('checked'):
            self.remember_me_link.click()
        self.submit_button.click()

    right_section = WebElement(id='page-right')

    form = WebElement(css_selector='.login-form-container form.login-form')
    form_title = WebElement(css_selector='.login-form-container h1')
    auth_select_menu = WebElement(css_selector='form.login-form .tabs-input-container__tabs')
    input_username = WebElement(id='username')
    input_password = WebElement(id='password')
    submit_button = WebElement(id='kc-login')

    sign_in_error = WebElement(id='form-error-message')
    input_username_error = WebElement(xpath='//span[contains(@class,"rt-input-container__meta--error")]')

    remember_me_link = WebElement(css_selector='span.rt-checkbox__label')
    remember_me_checkbox = WebElement(css_selector='input[name="rememberMe"]')
    forgot_password_link = WebElement(id='forgot_password')
    register_link = WebElement(id='kc-register')

    auth_select_menu_tabs = ManyWebElements(xpath='//div[contains(@class,"tabs-input-container__tabs")]/child::*')
    phone_tab = WebElement(id='t-btn-tab-phone')
    email_tab = WebElement(id='t-btn-tab-mail')
    login_tab = WebElement(id='t-btn-tab-login')
    ls_tab = WebElement(id='t-btn-tab-ls')

    input_username_placeholder = WebElement(xpath='//*[@id="username"]/following-sibling::*[contains(@class,"placeholder")]')
