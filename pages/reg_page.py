import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from pages.auth_page import AuthPage
from settings import Settings as settings


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or settings.base_url

        super().__init__(web_driver, url)

    def open(self):
        self.open_link.click()

    def register(
            self,
            first_name=settings.random_first_name,
            last_name=settings.random_last_name,
            email_phone=settings.random_email,
            password=settings.valid_password,
            confirm_password=settings.valid_password
    ):
        self.input_first_name.send_keys(first_name)
        self.input_last_name.send_keys(last_name)
        self.input_email_phone.send_keys(email_phone)
        self.input_password.send_keys(password)
        self.confirm_password.send_keys(confirm_password)
        self.submit_button.click()

    open_link = AuthPage.register_link

    left_section = WebElement(id='page-left')
    form = WebElement(css_selector='.register-form-container form.register-form')
    form_title = WebElement(css_selector='.register-form-container h1')
    input_first_name = WebElement(css_selector='input[name="firstName"]')
    input_last_name = WebElement(css_selector='input[name="lastName"]')
    select_region = WebElement(xpath='//div[contains(@class,"register-form__dropdown")]//input')
    input_email_phone = WebElement(id='address')
    input_password = WebElement(id='password')
    confirm_password = WebElement(id='password-confirm')
    submit_button = WebElement(xpath='//button[contains(@class,"register-form__reg-btn")]')
    policy_agreement_link = WebElement(css_selector='.auth-policy a')

    first_name_placeholder = WebElement(xpath='//input[@name="firstName"]/following-sibling::span[contains(@class,"placeholder")]')
    last_name_placeholder = WebElement(xpath='//input[@name="lastName"]/following-sibling::span[contains(@class,"placeholder")]')
    select_region_placeholder = WebElement(xpath='//div[contains(@class,"register-form__dropdown")]//span[contains(@class,"placeholder")]')
    email_phone_placeholder = WebElement(xpath='//input[@id="address"]/following-sibling::span[contains(@class,"placeholder")]')
    password_placeholder = WebElement(xpath='//input[@id="password"]/following-sibling::span[contains(@class,"placeholder")]')
    confirm_password_placeholder = WebElement(xpath='//input[@id="password-confirm"]/following-sibling::span[contains(@class,"placeholder")]')

    register_confirm_title = WebElement(css_selector='.register-confirm-form-container h1')
    register_confirm_description = WebElement(css_selector='.register-confirm-form-container p.register-confirm-form-container__desc')

    first_name_error = WebElement(xpath='//input[@name="firstName"]/ancestor::div[contains(@class,"error")]//span[contains(@class,"error")]')
    last_name_error = WebElement(xpath='//input[@name="lastName"]/ancestor::div[contains(@class,"error")]//span[contains(@class,"error")]')
    email_phone_error = WebElement(xpath='//div[contains(@class,"email-or-phone")]//span[contains(@class,"error")]')
    password_error = WebElement(xpath='//div[contains(@class,"__password")]//span[contains(@class,"error")]')
    confirm_password_error = WebElement(xpath='//div[contains(@class,"__confirmed-password")]//span[contains(@class,"error")]')

    modal = WebElement(css_selector='.card-modal__card')
    modal_title = WebElement(css_selector='.card-modal__card h2')
    modal_login_button = WebElement(css_selector='.card-modal__card button[name="gotoLogin"]')
    modal_restore_link = WebElement(id='reg-err-reset-pass')
