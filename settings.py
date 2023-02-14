class Settings:
    base_url = "https://b2c.passport.rt.ru"
    auth_page_path = "/auth/realms/b2c/protocol/openid-connect/auth"
    sign_in_error_path = "/auth/realms/b2c/login-actions/authenticate"
    user_account_page_path = "/account_b2c/page"
    restore_password_page_path = "/auth/realms/b2c/login-actions/reset-credentials"
    register_page_path = "/auth/realms/b2c/login-actions/registration"

    valid_email = "testbox@fexbox.org"
    valid_password = "P48sLPm28SLwq!J"
    unknown_email = "unknown@email.com"


class Expected:
    slogan_text = "Персональный помощник в цифровом мире Ростелекома"
    form_title_text = "Авторизация"
    submit_button_name = "Войти"
    forgot_password_link_text = "Забыл пароль"
    register_link_text = "Зарегистрироваться"
    tab_names = ["Номер", "Почта", "Логин", "Лицевой счёт"]
    phone_placeholder_text = "Мобильный телефон"
    email_placeholder_text = "Электронная почта"
    login_placeholder_text = "Логин"
    ls_placeholder_text = "Лицевой счёт"

    sign_in_error_text = "Неверный логин или пароль"
    email_error_text = "Введите адрес, указанный при регистрации"
    phone_error_text = "Введите номер телефона"
    login_error_text = "Введите логин, указанный при регистрации"
    ls_error_text = "Введите номер вашего лицевого счета"


class RegPageExpected:
    pass
