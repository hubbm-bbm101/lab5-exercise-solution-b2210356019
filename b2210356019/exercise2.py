def mail_check(mail):
    if "@" in mail and "." in mail:
        return True
    else:
        return False


user_mail = str(input("Please enter your email: "))
print(mail_check(user_mail))
