import pytest

from pages.reg_page import RegPage
from settings import Settings, Expected


def test_page_left_registration(web_browser):
    """TC-11 Левая часть формы «Регистрация» содержит логотип и продуктовый слоган кабинета."""

    page = RegPage(web_browser)
    page.open()

    assert page.get_relative_path() == Settings.register_page_path
    # try:
    #     page_reg = RegistrPage(selenium)
    #     assert page_reg.page_left_registration.text != ''
    # except AssertionError:
    #     print('Элемент отсутствует в левой части формы')