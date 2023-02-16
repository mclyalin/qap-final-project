import pytest

from pages.reg_page import RegPage
from settings import RegPageExpected as expected
from settings import Settings as settings


def test_page_left_section(web_browser):
    """TC-11 Левая часть формы «Регистрация» содержит логотип и продуктовый слоган кабинета."""

    page = RegPage(web_browser)
    page.open()
    blank = ""

    assert page.left_section.get_text() is not blank


def test_reg_form_elements(web_browser):
    """TC-12 Форма «Регистрация» содержит основные элементы: поля ввода, кнопка отправки формы, ссылки на политику конфиденциальности и пользовательское соглашение."""

    page = RegPage(web_browser)
    page.open()

    assert page.form.is_visible()
    assert page.input_first_name.is_clickable()
    assert page.input_last_name.is_clickable()
    assert page.select_region.is_clickable()
    assert page.input_email_phone.is_clickable()
    assert page.input_password.is_clickable()
    assert page.confirm_password.is_clickable()
    assert page.submit_button.is_clickable()
    assert page.policy_agreement_link.is_clickable()


def test_form_elements_names(web_browser):
    """TC-12_1 Названия элементов формы «Регистрация» соответствуют Требованиям."""

    page = RegPage(web_browser)
    page.open()

    assert page.form_title.get_text() == expected.form_title_text
    assert page.first_name_placeholder.get_text() == expected.first_name_placeholder_text
    assert page.last_name_placeholder.get_text() == expected.last_name_placeholder_text
    assert page.select_region_placeholder.get_text() == expected.select_region_placeholder_text
    assert page.email_phone_placeholder.get_text() == expected.email_phone_placeholder_text
    assert page.password_placeholder.get_text() == expected.password_placeholder_text
    assert page.confirm_password_placeholder.get_text() == expected.confirm_password_placeholder_text
    assert page.submit_button.get_text() == expected.submit_button_name


def test_register_user_by_email(web_browser):
    """TC-13 Регистрация пользователя по email"""

    page = RegPage(web_browser)
    page.open()
    page.register()

    assert page.register_confirm_title.get_text() == expected.confirm_email_title_text
    assert expected.confirm_email_description_text in page.register_confirm_description.get_text()


def test_register_user_by_phone(web_browser):
    """TC-14 Регистрация пользователя по телефону"""

    page = RegPage(web_browser)
    page.open()
    page.register(email_phone=settings.random_phone)

    assert page.register_confirm_title.get_text() == expected.confirm_phone_title_text
    assert expected.confirm_phone_description_text in page.register_confirm_description.get_text()


def test_register_user_by_blank_fields(web_browser):
    """TC-15 Регистрация пользователя с пустыми полями"""

    page = RegPage(web_browser)
    page.open()
    page.submit_button.click()

    assert page.get_relative_path() == settings.register_page_path
    assert page.first_name_error.get_text() == expected.name_error_text
    assert page.last_name_error.get_text() == expected.name_error_text
    assert page.email_phone_error.get_text() == expected.email_phone_error_text
    assert page.password_error.get_text() in expected.password_error_texts
    assert page.confirm_password_error.get_text() in expected.password_error_texts


def test_register_user_by_registered_email(web_browser):
    """TC-16 Регистрация пользователя по уже зарегистрированному email"""

    page = RegPage(web_browser)
    page.open()
    page.register(email_phone=settings.valid_email)

    assert page.get_relative_path() == settings.register_page_path
    assert page.modal.is_visible()
    assert page.modal_title.get_text() == expected.modal_title_text
    assert page.modal_login_button.is_clickable()
    assert page.modal_login_button.get_text() == expected.modal_button_name
    assert page.modal_restore_link.is_clickable()
    assert page.modal_restore_link.get_text() == expected.modal_restore_link_text


def test_modal_button_redirect_to_auth_page(web_browser):
    """TC-17 Модальное окно формы "Регистрация": проверка редиректа на страницу "Авторизация" по кнопке 'Войти'"""

    page = RegPage(web_browser)
    page.open()
    page.register(email_phone=settings.valid_email)
    page.modal_login_button.click()

    assert page.get_relative_path() == settings.sign_in_error_path


def test_modal_link_redirect_to_restore_page(web_browser):
    """TC-17_1 Модальное окно формы "Регистрация": проверка редиректа на страницу "Восстановление пароля" по ссылке 'Восстановить пароль'"""

    page = RegPage(web_browser)
    page.open()
    page.register(email_phone=settings.valid_email)
    page.modal_restore_link.click()

    assert page.get_relative_path() == settings.restore_password_page_path


@pytest.mark.parametrize("name", settings.valid_names.values(), ids=settings.valid_names.keys())
def test_first_name_by_valid_data(web_browser, name):
    """TC-18 Форма «Регистрация» поле "Имя": позитивная проверка (кириллица длиной 2,3,15,29,30, имя с тире)."""

    page = RegPage(web_browser)
    page.open()
    page.input_first_name.send_keys(name)
    page.input_last_name.click()

    assert not page.first_name_error.is_presented()


@pytest.mark.parametrize("name", settings.valid_names.values(), ids=settings.valid_names.keys())
def test_last_name_by_valid_data(web_browser, name):
    """TC-18_1 Форма «Регистрация» поле "Фамилия": позитивная проверка (кириллица длиной 2,3,15,29,30, имя с тире)."""

    page = RegPage(web_browser)
    page.open()
    page.input_last_name.send_keys(name)
    page.input_first_name.click()

    assert not page.last_name_error.is_presented()


@pytest.mark.parametrize("name", settings.invalid_names.values(), ids=settings.invalid_names.keys())
def test_first_name_by_invalid_data(web_browser, name):
    """TC-19 Форма «Регистрация» поле "Имя": негативный тест (кириллица длиной 1,31,500, латиница,иероглифы,спецсимволы,числа)."""

    page = RegPage(web_browser)
    page.open()
    page.input_first_name.send_keys(name)
    page.input_last_name.click()

    assert page.first_name_error.is_presented()
    assert page.first_name_error.get_text() == expected.name_error_text


@pytest.mark.parametrize("name", settings.invalid_names.values(), ids=settings.invalid_names.keys())
def test_last_name_by_invalid_data(web_browser, name):
    """TC-19_1 Форма «Регистрация» поле "Фамилия": негативный тест (кириллица длиной 1,31,500, латиница,иероглифы,спецсимволы,числа)."""

    page = RegPage(web_browser)
    page.open()
    page.input_last_name.send_keys(name)
    page.input_first_name.click()

    assert page.last_name_error.is_presented()
    assert page.last_name_error.get_text() == expected.name_error_text


@pytest.mark.parametrize("password", settings.valid_passwords.values(), ids=settings.valid_passwords.keys())
def test_password_by_valid_data(web_browser, password):
    """TC-20 Форма «Регистрация» поле "Пароль": позитивный тест (латиница+числа длиной 8,15,20)."""

    page = RegPage(web_browser)
    page.open()
    page.input_password.send_keys(password)
    page.confirm_password.click()

    assert not page.password_error.is_presented()


@pytest.mark.parametrize("password", settings.valid_passwords.values(), ids=settings.valid_passwords.keys())
def test_confirm_password_by_valid_data(web_browser, password):
    """TC-20_1 Форма «Регистрация» поле "Подтвердить пароль": позитивный тест (латиница+числа длиной 8,15,20)."""

    page = RegPage(web_browser)
    page.open()
    page.confirm_password.send_keys(password)
    page.input_password.click()

    assert not page.confirm_password_error.is_presented()


@pytest.mark.parametrize("password", settings.invalid_passwords.values(), ids=settings.invalid_passwords.keys())
def test_password_by_invalid_data(web_browser, password):
    """TC-21 Форма «Регистрация» поле "Пароль": негативный тест (длина 7,21, кириллица,прописные,строчные,буквы,цифры)"""

    page = RegPage(web_browser)
    page.open()
    page.input_password.send_keys(password)
    page.confirm_password.click()

    assert page.password_error.is_presented()
    assert page.password_error.get_text() in expected.password_error_texts


@pytest.mark.parametrize("password", settings.invalid_passwords.values(), ids=settings.invalid_passwords.keys())
def test_confirm_password_by_invalid_data(web_browser, password):
    """TC-21_1 Форма «Регистрация» поле "Подтвердить пароль": негативный тест (длина 7,21, кириллица,прописные,строчные,буквы,цифры)"""

    page = RegPage(web_browser)
    page.open()
    page.confirm_password.send_keys(password)
    page.input_password.click()

    assert page.confirm_password_error.is_presented()
    assert page.confirm_password_error.get_text() in expected.password_error_texts


def test_passwords_not_match_error(web_browser):
    """TC-22 Форма «Регистрация»: отправка формы с несовпадающими паролями"""

    page = RegPage(web_browser)
    page.open()
    page.register(password=settings.valid_password, confirm_password=settings.valid_password[::-1])

    assert page.get_relative_path() == settings.register_page_path
    assert page.confirm_password_error.is_presented()
    assert page.confirm_password_error.get_text() == expected.confirm_password_error_text
