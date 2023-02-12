from pages.auth_page import AuthPage
from settings import Expected


def test_page_right(web_browser):
    """TC-01 В правой части формы «Авторизация» находится продуктовый слоган ЛК "Ростелеком ID"."""

    page = AuthPage(web_browser)
    assert Expected.slogan_text in page.right_section.text, 'Слоган отсутствует в правой части формы'

def test_elements_of_auth(web_browser):
    """TC-02 Блок аутентификации формы «Авторизация» содержит основные элементы (Меню выбора типа аутентификации,
    Формы ввода, кнопка "Войти", ссылки "Забыл пароль" и "Зарегистрироваться")."""
    page = AuthPage(web_browser)

    assert page.left_section.is_displayed()
    # assert page.menu_tub.text in page.card_of_auth.text
    # assert page.email.text in page.card_of_auth.text
    # assert page.pass_eml.text in page.card_of_auth.text
    # assert page.btn_enter.text in page.card_of_auth.text
    # assert page.forgot_password_link.text in page.card_of_auth.text
    # assert page.register_link.text in page.card_of_auth.text
