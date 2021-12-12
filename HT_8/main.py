import csv

def csv_users(user_name,password):
    #перевірка введених логіну та паролю на зареєстрованих користувачів 
    with open('users.csv') as f:
        csv_reader = csv.reader(f,delimiter = ';')
        user_list = [i for i in csv_reader]
        for i in user_list:
            if i[0] == user_name and i[1] == password:
                return True
        return False
            
def check_user_balance(user_name):
    #перевірка на наявність балансу користувача
    try:
        open(f'{user_name}_balance.txt')
    except:
        with open(f'{user_name}_balance.txt', 'w') as f:
            f.write('0')
        
    #читання файлу балансу
    with open(f'{user_name}_balance.txt') as f:
        return f.readline()

def change_balance(user_name,summ):
    #запис нового балансу в файл для поповнення/зняття коштів
    balance = check_user_balance(user_name)
    result = int(balance) + summ
    if result < 0:
        print('A little money on the card')
        return False
    else:
        with open(f'{user_name}_balance.txt','w') as f:
            f.write(str(result))
            return True
    

def csv_transactions(user_name,type_transact,output):
    #запис в файл транзакцій
    header = ['Type of transaction', 'Output information']
    transact_dict = {header[0]:type_transact, header[1]:output}
    try:
        open(f'{user_name}_transactions.csv')
    except:
        with open (f'{user_name}_transactions.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f,delimiter = ';',fieldnames=header)
            writer.writeheader()
            f.close()
    with open (f'{user_name}_transactions.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f,delimiter = ';',fieldnames=header)
        writer.writerow(transact_dict)
        f.close()
        
def check_correct_summ(summ):
    #перевірка правильного введення суми юзером
    for i in summ:
        if i.isalpha():
            summ = input('Enter right sum, without symbols: ')
            break
    summ = abs(int(summ))
    return summ

def csv_denominations():
    #перегляд кількості номіналів у файлі
    list_denom = []
    with open('denominations.csv') as f:
        reader = csv.DictReader(f, delimiter = ';')
        for row in reader:
            list_denom.append(row)
    return list_denom
            
def change_count_denominations(denom):
    #зміна кількості номіналу
    list_denom = csv_denominations()
    dict_denom = list_denom[0]
    for i in dict_denom:
        if i not in denom:
            continue
        new_value = dict_denom.get(i)
        new_value = int(new_value) + int(denom.get(i))
        dict_denom.update({i:str(new_value)})
    header = ['10','20','50','100','200','500','1000']
    with open('denominations.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(header)
        writer.writerow(dict_denom.values())

def menu_collector():
    #меню для інкасатора
    print(' 1 - Check the balance ATM\n 2 - Change the balance ATM')
    user_option = input('Select an option: ')
    if user_option == '1':
        print(csv_denominations())
    elif user_option == '2':
        denom_list = [10,20,50,100,200,500,1000]
        input_denom = input(f'Enter denomination {denom_list} : ')
        input_denom = check_correct_summ(input_denom)
        if input_denom in denom_list:
            count_denom = input('Enter count for this denomination: ')
            count_denom = check_correct_summ(count_denom)
            denom_dict = {str(input_denom):str(count_denom)}
            change_count_denominations(denom_dict)
            print('Successful')
        else:
            print('Incorrect denomination')
    else:
        print('Incorrect option')

def output_denominations(summ):
    #алгоритм видачі номіналів
    new_list = []
    with open('denominations.csv') as f:
        reader = csv.DictReader(f, delimiter = ';')
        list_result = [i for i in reader]
    dict_result = list_result[0]
    list_result = list(dict_result.items())
    new_list = []
    for i in list_result:
        i = list(i)
        new_list.append(i)
    list_result.clear()
    for value in new_list:
        if (int(value[0]) * int(value[1])) == 0:
            continue
        list_result.append(value)
    list_result.reverse()
    a = []
    for i in list_result:
        if summ < int(i[0]):
            continue
        result = summ // int(i[0])
        if result < int(i[1]):
            summ = summ - (result * int(i[0]))
            k = int(i[1]) - result
            i.insert(1,k)
            i.pop()
        else:
            summ = summ - (int(i[1]) * int(i[0]))
            list_result.remove(i)
        while result > 0:
            a.append(i[0])
            result -= 1
    return a
            
           
def start():
    user_name = input('Enter login: ')
    password = input('Enter password: ')
    check_user_name_password = csv_users(user_name,password)
    if check_user_name_password == False:
        print('You entered incorrect login or password')
    elif check_user_name_password == True and user_name == 'collector':
        menu_collector()
    else:
        i = True
        while i:
            print(' 1 - Check the balance\n 2 - Top up your balance\n 3 - Take money\n 4 - Exit')
            user_option = input('Select an option: ')
            if user_option == '1':
                type_transact = 'Check the balance'
                output = check_user_balance(user_name)
                csv_transactions(user_name,type_transact,output)
                print(f'You have {output} money')
            elif user_option == '2':
                summ = input('How much do you want to top up? ')
                result = check_correct_summ(summ)
                change_balance(user_name,result)
                print('Money in your card =)')
                type_transact = 'Top up the balance'
                csv_transactions(user_name,type_transact,result)
            elif user_option == '3':
                summ = input('How much do you want to take money? ')
                result = check_correct_summ(summ)
                type_transact = 'Withdrawal of money'
                if change_balance(user_name,-result) == True:
                    denom = output_denominations(result)
                    print(denom)
                    denom = {i:-(denom.count(i)) for i in denom}
                    change_count_denominations(denom)
                    print(f'Put your money - {result}')
                    csv_transactions(user_name,type_transact,result)
                else:
                    result = f'Transaction is not successful - {result}'
                    csv_transactions(user_name,type_transact,result)
            elif user_option == '4':
                print('Exit')
                i = False
            else:
                print('Enter correct option')
                                            
start()
