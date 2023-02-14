import pytest

from pages.reg_page import RegPage
from settings import Settings, Expected


def test_page_left_registration(web_browser):
    """TC-11 Левая часть формы «Регистрация» содержит логотип и продуктовый слоган кабинета."""

    page = RegPage(web_browser)
    page.open()

    blank = ""
    assert page.left_section.get_text() is not blank

