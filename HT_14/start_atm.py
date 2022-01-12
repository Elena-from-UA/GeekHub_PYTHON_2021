import sqlite3
import itertools
import requests
import ATM as ATM
from main import *


def start():
    user_name = input('Enter login: ')
    password = input('Enter password: ')
    check_user_name_password = ATM()
    check_user_name_password = check_user_name_password.check_users(user_name,password)
    if check_user_name_password == False:
        print('You entered incorrect login or password')
        new_user = input('Do you want to register? (Y/N): ')
        if new_user == 'Y':
            new_user_login = input('Enter login: ')
            new_user_password = input('Enter password: ')
            user_is_admin = input('Are you collector? (Y/N): ')
            if user_is_admin == 'Y':
                user_is_admin = 1
                admin = Admin(new_user_login,new_user_password,user_is_admin)
            elif user_is_admin == 'N':
                user_is_admin = 0
                user = User(new_user_login,new_user_password,user_is_admin)
            else:
                print('You input incorrect symbols')
        elif new_user == 'N':
            print('EXIT')
        else:
            print('You input incorrect symbols')
    elif check_user_name_password == 'admin':
        while True:
            print(' 1 - Check the balance ATM\n 2 - Change the balance ATM\n 3 - Exit')
            user_option = input('Select an option: ')
            admin_atm = ATM()
            if user_option == '1':
                cur.execute('SELECT * FROM denominations')
                rows = cur.fetchall()
                print(rows)
            elif user_option == '2':
                denom_list = [10, 20, 50, 100, 200, 500, 1000]
                input_denom = input(f'Enter denomination {denom_list} : ')
                input_denom = check_correct_summ(input_denom)
                if input_denom in denom_list:
                    count_denom = input('Enter count for this denomination: ')
                    count_denom = check_correct_summ(count_denom)
                    denom = {input_denom: count_denom}
                    admin_atm.change_count_denominations(denom)
                    print('Successful')
                else:
                    print('Incorrect denomination')
            elif user_option == '3':
                return 'Exit'
            else:
                print('Incorrect option')
    else:
        while True:
            print(' 1 - Check the balance\n 2 - Top up your balance\n 3 - Take money\n 4 - Exchange Rates\n 5 - Exit')
            user_option = input('Select an option: ')
            menu = Menu()
            if user_option == '1':
                menu.check_the_balance(user_name)
            elif user_option == '2':
                summ = input('How much do you want to top up? ')
                result = check_correct_summ(summ)
                menu.top_up_user_balance(user_name,result)
            elif user_option == '3':
                summ = input('How much do you want to take money? ')
                result = check_correct_summ(summ)
                menu.take_money(user_name,result)
            elif user_option == '4':
                menu.exchange_rates()
            elif user_option == '5':
                return 'Exit'
            else:
                print('Enter correct option')
                
def check_correct_summ(summ):   
    # перевірка правильного введення суми юзером
    for i in summ:
        if i.isalpha():
            summ = input('Enter right sum, without symbols: ')
            break
    summ = abs(int(summ))
    return summ

print(start())
