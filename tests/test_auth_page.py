from pages.auth_page import AuthPage
from settings import Expected


# def test_page_right(web_browser):
#     """TC-01 В правой части формы «Авторизация» находится продуктовый слоган ЛК "Ростелеком ID"."""
#     page = AuthPage(web_browser)

#     assert Expected.slogan_text in page.right_section.get_text()


# def test_elements_of_auth(web_browser):
#     """TC-02 Блок аутентификации формы «Авторизация» содержит основные элементы (Меню выбора типа аутентификации,
#     Поля ввода, кнопка "Войти", ссылки "Забыл пароль" и "Зарегистрироваться")."""
#     page = AuthPage(web_browser)

#     assert page.form.is_visible()
#     assert page.form_title.get_text() == 'Авторизация'
#     assert page.auth_type_menu.is_visible()
#     assert page.input_username.is_clickable()
#     assert page.input_password.is_clickable()
#     assert page.submit_button.is_clickable()
#     assert page.submit_button.get_text() == 'Войти'
#     assert page.forgot_password_link.is_clickable()
#     assert page.forgot_password_link.get_text() == 'Забыл пароль'
#     assert page.register_link.is_clickable()
#     assert page.register_link.get_text() == 'Зарегистрироваться'


# def test_menu_of_type_auth(web_browser):
#     """TC-03 Меню выбора типа аутентификации содержит табы: 'Номер', 'Почта', 'Логин', 'Лицевой счёт'."""
#     page = AuthPage(web_browser)

#     tab_names = page.auth_type_menu_tabs.get_text()
#     assert tab_names == Expected.tab_names


# def test_menu_of_type_active_auth(web_browser):
#     """TC-04 В Меню выбора типа аутентификации по умолчанию выбрана форма аутентификации по телефону."""
#     page = AuthPage(web_browser)

#     phone_tab_class = page.phone_tab.get_attribute('class')
#     assert 'active' in phone_tab_class


# def test_placeholder_name_of_user(web_browser):
#     """TC-05 В форме ввода ('Номер', 'Почта', 'Логин', 'Лицевой счёт') плейсхолдер меняется в соответствии с
#     выбранным табом Меню."""
#     page = AuthPage(web_browser)

#     page.phone_tab.click()
#     assert page.input_username_placeholder.get_text() == 'Мобильный телефон'

#     page.email_tab.click()
#     assert page.input_username_placeholder.get_text() == 'Электронная почта'

#     page.login_tab.click()
#     assert page.input_username_placeholder.get_text() == 'Логин'

#     page.ls_tab.click()
#     assert page.input_username_placeholder.get_text() == 'Лицевой счёт'

# def test_forgot_password_link(web_browser):
#     """TC-06 Проверка перехода по ссылке 'Забыл пороль'."""
#     page = AuthPage(web_browser)

#     page.forgot_password_link.click()
#     assert page.get_relative_path() == '/auth/realms/b2c/login-actions/reset-credentials'


def test_register_link(web_browser):
    """TC-07 Проверка перехода по ссылке 'Зарегистрироваться'."""

    page = AuthPage(web_browser)
    page.register_link.click()

    assert page.get_relative_path() == '/auth/realms/b2c/login-actions/registration'
