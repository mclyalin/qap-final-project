class Settings:
    base_url = "https://" + "b2c.passport.rt.ru"
    auth_page_path = "/auth/realms/b2c/protocol/openid-connect/auth"
    sign_in_error_path = "/auth/realms/b2c/login-actions/authenticate"
    user_account_page_path = "/account_b2c/page"
    restore_password_page_path = "/auth/realms/b2c/login-actions/reset-credentials"
    register_page_path = "/auth/realms/b2c/login-actions/registration"

    valid_email = "testbox@" + "fexbox.org"
    valid_password = "P48sLPm28SLwq" + "!J"

    # valid_first_name = "Тестер"
    # valid_last_name = "Тестеров"

    random_email = "unknown@" + "email.com"
    random_phone = "+7 901 " + "249-22-49"
    random_first_name = "Имя"
    random_last_name = "Фамилия"

    ru_char = "ж"
    en_chars = "asdfgh"
    cn_chars = "不会说汉怎"
    spec_chars = "!@#${*"
    numbers = "1234"

    valid_names = {
        'ru_char_2': ru_char * 2,
        'ru_char_3': ru_char * 3,
        'ru_char_15': ru_char * 15,
        'ru_char_29': ru_char * 29,
        'ru_char_30': ru_char * 30,
        'with_dash': f'{ru_char * 2}-{ru_char * 2}',
    }

    valid_passwords = {
        'pass_8': 'IRCC1nk1',
        'pass_14': 'aMJHO3E6aWrYGC',
        'pass_20': '43MyK7tkhu99N6cTFa6G'
    }


    invalid_names = {
        'ru_char': ru_char,
        'ru_char_31': ru_char * 31,
        'ru_char_500': ru_char * 500,
        'en_chars': en_chars,
        'cn_chars': cn_chars,
        'spec_chars': spec_chars,
        'numbers': numbers,
    }

    invalid_passwords = {
        'pass_7': 'FuduyMQ',
        'pass_21': '9uM6XPVEN3790tf6YqKna',
        'pass_ru': 'fДl0VTЗVгг',
        'pass_low': 'y3tks1i08n',
        'pass_cap': '5VWJZMIKXB',
        'pass_let': 'OUKEGhtfyD',
        'pass_dig': '8755042810',
    }


class AuthPageExpected:
    slogan_text = "Персональный помощник в цифровом мире Ростелекома"
    form_title_text = "Авторизация"
    submit_button_name = "Зарегистрироваться"
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
    form_title_text = "Регистрация"

    first_name_placeholder_text = "Имя"
    last_name_placeholder_text = "Фамилия"
    select_region_placeholder_text = "Регион"
    email_phone_placeholder_text = "E-mail или мобильный телефон"
    password_placeholder_text = "Пароль"
    confirm_password_placeholder_text = "Подтверждение пароля"
    submit_button_name = "Продолжить"

    confirm_email_title_text = "Подтверждение email"
    confirm_email_description_text = "Kод подтверждения отправлен на адрес"
    confirm_phone_title_text = "Подтверждение телефона"
    confirm_phone_description_text = "Kод подтверждения отправлен на номер"

    name_error_text = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    email_phone_error_text = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    password_error_texts = [
        "Длина пароля должна быть не менее 8 символов",
        "Длина пароля должна быть не более 20 символов",
        "Пароль должен содержать только латинские буквы",
        "Пароль должен содержать хотя бы одну заглавную букву",
        "Пароль должен содержать хотя бы одну прописную букву",
        "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру",
    ]
    confirm_password_error_text = "Пароли не совпадают"

    modal_title_text = "Учётная запись уже существует"
    modal_button_name = "Войти"
    modal_restore_link_text = "Восстановить пароль"
