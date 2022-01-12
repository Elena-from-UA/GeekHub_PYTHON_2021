import sqlite3
import itertools
import requests
import ATM as ATM

try:
    con = sqlite3.connect('ATM.db')
    cur = con.cursor()
    print("База данных успешно подключена к SQLite")

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    
ATM.create_BD(cur,con)


class ATM(object):

    def change_count_denominations(self,denom):
        self.denom = denom
        cur.execute('SELECT * FROM denominations')
        rows = cur.fetchall()
        list_denom = rows
        dict_denom = {i[0]:i[1] for i in list_denom}
        result_list = []
        for i in dict_denom:
            if i not in self.denom:
                continue
            new_value = dict_denom.get(i)
            new_value = int(new_value) + int(self.denom.get(i))
            dict_denom.update({i: new_value})
        for i in dict_denom:
            result_list.append((dict_denom.get(i),i))
        cur.executemany('''UPDATE denominations SET denom_balance = ?
                        WHERE denom_name = ? ''',result_list)
        con.commit()

    def output_denominations(self,summ):
        self.summ = summ
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
            if self.summ < i:
                continue
            result = self.summ // i
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
        
    def check_users(self,user_name,password):
        self.user_name = user_name
        self.password = password
        cur.execute('SELECT * from users')
        rows = cur.fetchall()
        for i in rows:
            if i[0] == self.user_name and i[1] == self.password:
                if i[2] == 1:
                    return 'admin'
                return True
        return False
    
class Person(object):
    
    def __init__(self, user_name, password, is_admin):
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
        user = (self.user_name,self.password,self.is_admin)
        cur.execute("INSERT INTO users VALUES (?,?,?)",user)
        con.commit()
        cur.execute("INSERT INTO balance VALUES (?,?)",(user_name,0))
        con.commit()
        
    def check_user_balance(self,user_name):
        self.user_name = user_name
        cur.execute('SELECT * from balance')
        rows = cur.fetchall()
        for i in rows:
            if i[0] == self.user_name:
                return i[1]
            if i[1] is None:
                i[0] = 0
        return False
    
    def users_transactions(self,user_name, type_transact, output):
        self.user_name = user_name
        self.type_transact = type_transact
        self.output = output
        cur.execute('''INSERT INTO transactions(user_login,transaction_name,transaction_information)
                    VALUES (?,?,?) ''',(user_name, type_transact, output))
        con.commit()
        
    def change_balance(self,summ,balance):
        self.balance = balance
        self.summ = summ
        result = self.balance + self.summ
        if result < 0 or result == False:
            print('A little money on the card')
            return False
        else:
            cur.execute('''UPDATE balance SET user_balance = ?
                    WHERE user_login = ? ''',(result,self.user_name))
            con.commit()
            return True
    
class User(Person):

    def __init__(self, user_name, password, is_admin):
        super().__init__(user_name, password, is_admin)

class Admin(Person):
    
    def __init__(self, user_name, password, is_admin):
        super().__init__(user_name, password, is_admin)

class Menu(object):

    def check_the_balance(self,user_name):
        self.user_name = user_name
        type_transact = 'Check the balance'
        output = Person.check_user_balance(self,user_name)
        Person.users_transactions(self,user_name,type_transact,output)
        print(f'You have {output} money')

    def top_up_user_balance(self,user_name,result):
        self.user_name = user_name
        balance = Person.check_user_balance(self,user_name)
        Person.change_balance(self,result,balance)
        print('Money in your card =)')
        type_transact = 'Top up the balance'
        Person.users_transactions(self,user_name, type_transact, result)

    def take_money(self,user_name,result):
        self.user_name = user_name
        type_transact = 'Withdrawal of money'
        denom = ATM.output_denominations(self,result)
        if denom == False:
            print('ATM can`t give you this sum')
        else:
            balance = Person.check_user_balance(self,user_name)
            if Person.change_balance(self,-result,balance) == True:
                print(denom)
                denom = {i: -(denom.count(i)) for i in denom}
                ATM.change_count_denominations(self,denom)
                print(f'Put your money - {result}')
                Person.users_transactions(self,user_name, type_transact, result)
            else:
                result = f'Transaction is not successful - {result}'
                Person.users_transactions(self,user_name, type_transact, result)

    def exchange_rates(self):
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        res = requests.get(url)
        if res.status_code != 200:
            raise Exception("ERROR: API rquest unsuccessful.")
        data = res.json()
        for i in data:
            print(i)
            

