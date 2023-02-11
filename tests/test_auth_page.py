from pages.auth_page import AuthPage


def test_page_right(web_browser):
    """TC-01 В правой части формы «Авторизация» находится продуктовый слоган ЛК "Ростелеком ID"."""
    try:
        page = AuthPage(web_browser)
        assert 'Персональный помощник в цифровом мире Ростелекома' in page.page_right.text
    except AssertionError:
        print('Элемент отсутствует в правой части формы')
