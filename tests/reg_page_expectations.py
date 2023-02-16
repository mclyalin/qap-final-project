class RegPageExpectations:
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
