'''Банкомат (Task 1)'''

def user_name_file():
    #отримати логіни та паролі користувачів з файлу та передати їх у список
    user_list = []
    with open('users.txt') as f:
        for line in f.readlines():
            i = line.split(',')
            user_list.append(i)
        for pw in user_list:
            i = int(pw[1])
            pw.insert(1,i)
            pw.pop()
            
    return user_list        

def check_user_balance_file(user_name):
    #створюється/читається файл та повертає баланс користувача
    try:
        file = open(f'{user_name}_balance.txt','r')
    except:
        file = open(f'{user_name}_balance.txt','w')
    with open(f'{user_name}_balance.txt','r') as f:
        return f.readline()
    
def top_up_user_balance_file(user_name,summ):
    #читається файл та перезаписується нова сума
    with open(f'{user_name}_balance.txt','r') as f:
        total_summ = f.readline()
        if total_summ == '':
            total_summ = 0
        else:
            total_summ = int(total_summ) + summ
    with open(f'{user_name}_balance.txt','w') as f:
        f.write(str(total_summ))

def take_user_balance_file(user_name,summ):
    #читається файл, перевіряється чи вказана сума не більше суми у файлі, та перезаписується у разі успішного виконання умови
    with open(f'{user_name}_balance.txt','r') as f:
        total_summ = f.readline()
        if total_summ == '' or int(total_summ) < summ:
            print('A little money in your card')
        else:
            total_summ = int(total_summ) - summ
            print(f'Put your money - {summ}')
    with open(f'{user_name}_balance.txt','w') as f:
        f.write(str(total_summ))
               
    
def start():
    #Введений користувачем логін та пароль розбивається у список для подальшої перевірки його у списку user_list функції user_name_file
    user_name = input('Enter your login and password, divide them ",": ')
    try:
        user_name = user_name.split(',')
    except:
        print('You enter incorrect login/password! Need format "login,password"')
    try:
        i = int(user_name[1])
        user_name.insert(1,i)
        user_name.pop()
    except:
        print('Password must have only numbers')
    
    check_user = user_name_file()
    
    #створення циклу постійного виконання програми, поки не буде обрано вихід з програми
    i = True
    while i:
        if user_name in check_user:
            user_change = input("Enter action\n 1 - Check the balance\n 2 - Top up your balance\n 3 - Take money\n 4 - Exit: ")
            if user_change == '1':
                #user_name[0] - логін користувача
                check_balance = check_user_balance_file(user_name[0])   
                print(f'You have {check_balance} money')
                #запис в файл транзакції
                with open(f'{user_name[0]}_transactions.txt','a') as f:
                    dict_transact = {'Check the balance': check_balance}
                    f.write(str(dict_transact))
                    f.write('\n')
            elif user_change == '2':
                summ = input('How much do you want to top up? ')
                for i in summ:
                    if i.isalpha():
                        summ = input('Enter right sum, without symbols: ')
                        break
                summ = int(summ)
                top_up_balance = top_up_user_balance_file(user_name[0],summ)
                print('Money in your card =)')
                with open(f'{user_name[0]}_transactions.txt','a') as f:
                    dict_transact = {'Input sum': summ}
                    f.write(str(dict_transact))
                    f.write('\n')
            elif user_change == '3':
                summ = input('How much do you want to take? ')
                for i in summ:
                    if i.isalpha():
                        summ = input('Enter right sum, without symbols: ')
                        break
                summ = int(summ)
                take_money = take_user_balance_file(user_name[0],summ)
                with open(f'{user_name[0]}_transactions.txt','a') as f:
                    if take_money is None:
                        take_money = 'Transaction is not successful'
                    dict_transact = {'Output sum': take_money}
                    f.write(str(dict_transact))
                    f.write('\n')
            elif user_change == '4':
                #Вихід з програми за бажанням користувача
                print('Put your card')
                i = False
            else:
                print('Enter right action')
        else:
            #Вихід з програми у разі неправильно вказаного логіну/паролю
            print('Incorrect login or password')
            print('Exit')
            i = False
      
       
start()

