''' Task 3
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів
       (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
       перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)'''

class InvalidUsername(Exception):
    pass
    
class InvalidPassword(Exception):
    pass

class CapsLock(Exception):
    pass

def check_user():
    dict_user = {'super_ivan':'qwerty', 'ANTONIO97':'gtyKL12df', 'super_user':'admin0000', 'gh':'fghjk123'}
    
    for value in dict_user.values():
        for i in value:
            if i.isdigit():
                bool_check_pw = i.isdigit()
            else:
                bool_check_pw = False
            
    for username in dict_user:
        print(f'Name: {username}')
        print(f'Password: {dict_user.get(username)}')
             
        try:
            if len(username) < 3 or len(username) > 50:
                raise InvalidUsername()
            if len(dict_user.get(username)) < 8 or bool_check_pw == False:
                raise InvalidPassword()
            if username.isupper():
                raise CapsLock()
        except InvalidUsername:
            print('Status: Username must have lenght between 3 and 50')
        except InvalidPassword:
            print('Status: Password must have lenght > 8 and consist a number')
        except CapsLock:
            print('Status: You entered your username with CapsLock')
        else:
            print('Status: OK')
        finally:
            print('-'*20)
    
       
print(check_user())
