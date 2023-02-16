class Settings:
    base_url = "https://" + "b2c.passport.rt.ru"
    auth_page_path = "/auth/realms/b2c/protocol/openid-connect/auth"
    sign_in_error_path = "/auth/realms/b2c/login-actions/authenticate"
    user_account_page_path = "/account_b2c/page"
    restore_password_page_path = "/auth/realms/b2c/login-actions/reset-credentials"
    register_page_path = "/auth/realms/b2c/login-actions/registration"


    valid_email = "testbox@" + "fexbox.org"
    valid_password = "P48sLPm28SLwq" + "!J"

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
