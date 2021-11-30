''' Task 1
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> -
       функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException'''

class LoginException(Exception):
    pass

def check_user(username,password,silent=False):
    dict_user = {'Ivan Petrov':0000, 'Olga Petrova':1234, 'Vasiliy Shevchenko':5555,
                 'Irina Shevchenko':7777, 'Sergey Ivanov':9876}
    if (username in dict_user.keys()) and (dict_user.get(username) == password):
        return True
    elif silent == True:
        return False
    else:
        raise LoginException('error')
    
        
print(check_user('Ivan Petrov', 2000))
