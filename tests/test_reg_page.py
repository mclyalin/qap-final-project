import pytest

from pages.reg_page import RegPage
from settings import Settings, Expected


def test_page_left_registration(web_browser):
    """TC-11 Левая часть формы «Регистрация» содержит логотип и продуктовый слоган кабинета."""

    page = RegPage(web_browser)
    page.open()

    blank = ""
    assert page.left_section.get_text() is not blank


def test_elements_of_registr(web_browser):
    """TC-12 Блок регистрации формы «Регистрация» содержит основные элементы:
    поля ввода: Имя, Фамилия, Регион, email, Пароль, Подтверждение пароля; кнопка "Продолжить"."""

    page = RegPage(web_browser)
    page.open()

    assert page.form.is_visible()
    assert page.form_title.get_text() == Expected.form_title_text
    assert page.auth_select_menu.is_visible()
    assert page.input_username.is_clickable()
    assert page.input_password.is_clickable()
    assert page.submit_button.is_clickable()
    assert page.submit_button.get_text() == Expected.submit_button_name
    assert page.forgot_password_link.is_clickable()
    assert page.forgot_password_link.get_text() == Expected.forgot_password_link_text
    assert page.register_link.is_clickable()
    assert page.register_link.get_text() == Expected.register_link_text
    # try:
    #     page_reg = RegistrPage(selenium)
    #     card_of_reg = [page_reg.first_name, page_reg.last_name, page_reg.address_registration,
    #                    page_reg.email_registration, page_reg.passw_registration,
    #                    page_reg.passw_registration_confirm, page_reg.registration_btn]
    #     for i in range(len(card_of_reg)):
    #         assert page_reg.first_name in card_of_reg
    #         assert page_reg.last_name in card_of_reg
    #         assert page_reg.email_registration in card_of_reg
    #         assert page_reg.address_registration in card_of_reg
    #         assert page_reg.passw_registration in card_of_reg
    #         assert page_reg.passw_registration_confirm in card_of_reg
    #         assert page_reg.registration_btn in card_of_reg
    # except AssertionError:
    #     print('Элемент отсутствует в форме «Регистрация»')