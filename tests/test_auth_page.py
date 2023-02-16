import pytest

from pages.auth_page import AuthPage
from settings import Settings as settings
from tests.auth_page_expectations import AuthPageExpectations as expected


def test_page_right_section(web_browser):
    """TC-01 В правой части формы «Авторизация» находится продуктовый слоган ЛК "Ростелеком ID"."""

    page = AuthPage(web_browser)

    assert expected.slogan_text in page.right_section.get_text()


def test_auth_form_elements(web_browser):
    """TC-02 Форма «Авторизация» содержит основные элементы: Выбор типа аутентификации, Поля ввода, кнопка входа, ссылки "Забыл пароль" и "Зарегистрироваться")."""

    page = AuthPage(web_browser)

    assert page.form.is_visible()
    assert page.form_title.get_text() == expected.form_title_text
    assert page.auth_select_menu.is_visible()
    assert page.input_username.is_clickable()
    assert page.input_password.is_clickable()
    assert page.submit_button.is_clickable()
    assert page.submit_button.get_text() == expected.submit_button_name
    assert page.forgot_password_link.is_clickable()
    assert page.forgot_password_link.get_text() == expected.forgot_password_link_text
    assert page.register_link.is_clickable()
    assert page.register_link.get_text() == expected.register_link_text


def test_auth_select_menu_tabs(web_browser):
    """TC-03 Меню выбора типа аутентификации содержит табы: 'Номер', 'Почта', 'Логин', 'Лицевой счёт'."""

    page = AuthPage(web_browser)
    tab_names = page.auth_select_menu_tabs.get_text()

    assert tab_names == expected.tab_names


def test_menu_active_tab_by_default(web_browser):
    """TC-04 В Меню выбора типа аутентификации по умолчанию выбрана форма аутентификации по телефону."""

    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute('class')

    assert 'active' in phone_tab_class


def test_username_placeholder_changes(web_browser):
    """TC-05 В поле ввода Типа авторизации плейсхолдер меняется в соответствии с выбранным табом Меню."""

    page = AuthPage(web_browser)

    page.phone_tab.click()
    assert page.input_username_placeholder.get_text() == expected.phone_placeholder_text

    page.email_tab.click()
    assert page.input_username_placeholder.get_text() == expected.email_placeholder_text

    page.login_tab.click()
    assert page.input_username_placeholder.get_text() == expected.login_placeholder_text

    page.ls_tab.click()
    assert page.input_username_placeholder.get_text() == expected.ls_placeholder_text


def test_forgot_password_link(web_browser):
    """TC-06 Проверка перехода по ссылке 'Забыл пароль'."""

    page = AuthPage(web_browser)
    page.forgot_password_link.click()

    assert page.get_relative_path() == settings.restore_password_page_path


def test_register_link(web_browser):
    """TC-07 Проверка перехода по ссылке 'Зарегистрироваться'."""

    page = AuthPage(web_browser)
    page.register_link.click()

    assert page.get_relative_path() == settings.register_page_path


@pytest.mark.xfail(reason="Тест может упасть из-за появления капчи")
def test_sign_in_by_valid_user(web_browser):
    """TC-08 Авторизация с валидными email и паролем."""

    page = AuthPage(web_browser)
    page.sign_in(settings.valid_email, settings.valid_password)

    assert page.get_relative_path() == settings.user_account_page_path


@pytest.mark.xfail(reason="Тест может упасть из-за появления капчи")
def test_sign_in_by_unknown_user(web_browser):
    """TC-09 Авторизация незарегистрированного пользователя"""

    page = AuthPage(web_browser)
    page.sign_in(settings.random_email, settings.valid_password)

    assert page.get_relative_path() == settings.sign_in_error_path
    assert page.sign_in_error.get_text() == expected.sign_in_error_text
    page.sign_in(settings.valid_email, settings.valid_password)


def test_sign_in_by_blank_fields(web_browser):
    """TC-10 Авторизация с пустыми полями"""

    page = AuthPage(web_browser)
    blank = ""

    page.phone_tab.click()
    page.sign_in(blank, blank)
    assert page.get_relative_path() == settings.auth_page_path
    assert page.input_username_error.get_text() == expected.phone_error_text

    page.email_tab.click()
    page.sign_in(blank, blank)
    assert page.get_relative_path() == settings.auth_page_path
    assert page.input_username_error.get_text() == expected.email_error_text

    page.login_tab.click()
    page.sign_in(blank, blank)
    assert page.get_relative_path() == settings.auth_page_path
    assert page.input_username_error.get_text() == expected.login_error_text

    page.ls_tab.click()
    page.sign_in(blank, blank)
    assert page.get_relative_path() == settings.auth_page_path
    assert page.input_username_error.get_text() == expected.ls_error_text
