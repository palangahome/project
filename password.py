def check_password(password):
    if len(password)>8:
        print('yes')
        return True
    else:
        print('no')
        return False
    
password=input(' пароль')


while check_password(password)==False:
    print('новый пароль')
    password=input(' пароль')
    
    