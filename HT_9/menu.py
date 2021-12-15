import sqlite3
import features as ft

def menu_collector(con):
    # меню для інкасатора
    cur = con.cursor()
    print(' 1 - Check the balance ATM\n 2 - Change the balance ATM')
    user_option = input('Select an option: ')
    if user_option == '1':
        print(ft.check_denominations(con))
    elif user_option == '2':
        denom_list = [10, 20, 50, 100, 200, 500, 1000]
        input_denom = input(f'Enter denomination {denom_list} : ')
        input_denom = ft.check_correct_summ(input_denom)
        if input_denom in denom_list:
            count_denom = input('Enter count for this denomination: ')
            count_denom = ft.check_correct_summ(count_denom)
            denom_dict = {input_denom: count_denom}
            ft.change_count_denominations(denom_dict,con)
            print('Successful')
        else:
            print('Incorrect denomination')
    else:
        print('Incorrect option')


def start(con):
    cur = con.cursor()
    user_name = input('Enter login: ')
    password = input('Enter password: ')
    check_user_name_password = ft.check_users(user_name, password,con)
    if check_user_name_password == False:
        print('You entered incorrect login or password')
        new_user = input('Do you want to register? (Y/N): ')
        if new_user == 'Y':
            new_user_login = input('Enter login: ')
            new_user_password = input('Enter password: ')
            user_is_admin = input('Are you collector? (Y/N): ')
            if user_is_admin == 'Y':
                user_is_admin = 1
                ft.register_user(new_user_login,new_user_password,user_is_admin,con)
            elif user_is_admin == 'N':
                user_is_admin = 0
                ft.register_user(new_user_login,new_user_password,user_is_admin,con)
            else:
                print('You input incorrect symbols')
            
        elif new_user == 'N':
            print('EXIT')
        else:
            print('You input incorrect symbols')
    elif check_user_name_password == 'admin':
        menu_collector(con)
    else:
        i = True
        while i:
            print(' 1 - Check the balance\n 2 - Top up your balance\n 3 - Take money\n 4 - Exit')
            user_option = input('Select an option: ')
            if user_option == '1':
                type_transact = 'Check the balance'
                output = ft.check_user_balance(user_name,con)
                ft.users_transactions(user_name, type_transact, output,con)
                print(f'You have {output} money')
            elif user_option == '2':
                summ = input('How much do you want to top up? ')
                result = ft.check_correct_summ(summ)
                ft.change_balance(user_name, result,con)
                print('Money in your card =)')
                type_transact = 'Top up the balance'
                ft.users_transactions(user_name, type_transact, result,con)
            elif user_option == '3':
                summ = input('How much do you want to take money? ')
                result = ft.check_correct_summ(summ)
                type_transact = 'Withdrawal of money'
                denom = ft.output_denominations(result,con)
                if denom == False:
                    print('ATM can`t give you this sum')
                else:
                    if ft.change_balance(user_name, -result,con) == True:
                        print(denom)
                        denom = {i: -(denom.count(i)) for i in denom}
                        ft.change_count_denominations(denom,con)
                        print(f'Put your money - {result}')
                        ft.users_transactions(user_name, type_transact, result,con)
                    else:
                        result = f'Transaction is not successful - {result}'
                        ft.users_transactions(user_name, type_transact, result,con)
            elif user_option == '4':
                print('Exit')
                i = False
            else:
                print('Enter correct option')
