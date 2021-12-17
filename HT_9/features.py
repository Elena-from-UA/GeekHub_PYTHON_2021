import sqlite3
import itertools

def register_user(user_name,password,is_admin,con):
    # реєстрація нового користувача
    cur = con.cursor()
    user = (user_name,password,is_admin)
    cur.execute("INSERT INTO users VALUES (?,?,?)",user)
    con.commit()
    cur.execute("INSERT INTO balance VALUES (?,?)",(user_name,0))
    con.commit()
    
def check_users(user_name, password,con):   
    # перевірка введених логіну та паролю на зареєстрованих користувачів
    cur = con.cursor()
    cur.execute('SELECT * from users')
    rows = cur.fetchall()
    for i in rows:
        if i[0] == user_name and i[1] == password:
            if i[2] == 1:
                return 'admin'
            return True
    return False        

def check_user_balance(user_name,con):  
    # виведення балансу користувача
    cur = con.cursor()
    cur.execute('SELECT * from balance')
    rows = cur.fetchall()
    for i in rows:
        if i[0] == user_name:
            return i[1]
        if i[1] is None:
            i[0] = 0
    return False

def change_balance(user_name, summ,con):    
    # запис нового балансу в файл для поповнення/зняття коштів
    cur = con.cursor()
    balance = check_user_balance(user_name,con)
    result = balance + summ
    if result < 0 or result == False:
        print('A little money on the card')
        return False
    else:
        cur.execute('''UPDATE balance SET user_balance = ?
                    WHERE user_login = ? ''',(result,user_name))
        con.commit()
        return True

def users_transactions(user_name, type_transact, output,con):   
    # запис в файл транзакцій
    cur = con.cursor()
    cur.execute('''INSERT INTO transactions(user_login,transaction_name,transaction_information)
                    VALUES (?,?,?) ''',(user_name, type_transact, output))
    con.commit()

def check_correct_summ(summ):   
    # перевірка правильного введення суми юзером
    for i in summ:
        if i.isalpha():
            summ = input('Enter right sum, without symbols: ')
            break
    summ = abs(int(summ))
    return summ

def check_denominations(con):  
    # перегляд кількості номіналів у файлі
    cur = con.cursor()
    cur.execute('SELECT * FROM denominations')
    rows = cur.fetchall()
    return rows

def change_count_denominations(denom,con):  
    # зміна кількості номіналу
    cur = con.cursor()
    list_denom = check_denominations(con)
    dict_denom = {i[0]:i[1] for i in list_denom}
    result_list = []
    for i in dict_denom:
        if i not in denom:
            continue
        new_value = dict_denom.get(i)
        new_value = int(new_value) + int(denom.get(i))
        dict_denom.update({i: new_value})
    for i in dict_denom:
        result_list.append((dict_denom.get(i),i))
    cur.executemany('''UPDATE denominations SET denom_balance = ?
                    WHERE denom_name = ? ''',result_list)
    con.commit()

def output_denominations(summ,con): 
    # алгоритм видачі номіналів
    cur = con.cursor()
    new_list = []
    cur.execute('SELECT * FROM denominations')
    rows = cur.fetchall()
    list_result = rows
    
    for i in list_result:
        i = list(i)
        new_list.append(i)
    new_list.reverse()
    list_result.clear()
    new_list = dict(new_list)
    b = {}

    for i in new_list:
        if new_list.get(i) == 0:
            continue
        if summ < i:
            continue
        result = summ // i
        if result == 0:
            continue
        if result > new_list.get(i):
            result = new_list.get(i)
        b.update({i:result})
    d = b.copy()
    l = []
    for i in b:
        z = b.get(i)
        while z > 0:
            l.append(i)
            z -= 1
            
    for L in range(0, len(l)+1):
        for subset in itertools.combinations(l, L):
            if sum(subset) == summ:
                if subset not in list_result:
                    list_result.append(subset)
    if len(list_result) == 0:
        return False
    new_dict = {}                
    for i in list_result:
        new_dict.update({len(i):i})

    best_result = min(new_dict.keys())

    return new_dict.get(best_result)

