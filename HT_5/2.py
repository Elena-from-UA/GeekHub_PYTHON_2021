''' Task 2
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.'''

class InvalidUsername(Exception):
    pass
    
class InvalidPassword(Exception):
    pass

class CapsLock(Exception):
    pass

def check_user(username,password):
    for i in password:
        if i.isdigit():
            bool_check_pw = i.isdigit()
            break
        else:
            bool_check_pw = False
        
    if len(username) < 3 or len(username) > 50:
        raise InvalidUsername('Username must have lenght between 3 and 50')
    
    if len(password) < 8 or bool_check_pw == False:
        raise InvalidPassword('Password must have lenght > 8 and consist a number')
    
    if username.isupper():
        raise CapsLock('You entered your username with CapsLock')
    
       
print(check_user(input('Enter username: '),input('Enter password: ')))
