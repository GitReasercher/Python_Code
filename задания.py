import sys as s

def new_user(password):

    has_letter = False

    has_digit = False

    for i in password:
        if i.isdigit():
            has_digit = True
            break

    for i in password:
        if i.isalpha:
            has_letter = True
            break

    password_long = 8
    if password < password_long:
        s.exit('В пароле должно быть минимум 8 символов, включая: буквы, цифры')


