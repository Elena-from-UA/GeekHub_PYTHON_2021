import sqlite3
import menu as m

try:
    con = sqlite3.connect('ATM.db')
    cur = con.cursor()
    print("База данных успешно подключена к SQLite")

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


cur.execute('''CREATE TABLE IF NOT EXISTS users
               (login TEXT NOT NULL PRIMARY KEY,
               password TEXT NOT NULL,
               collector BOOLEAN NOT NULL CHECK (collector IN (0,1)))''')

cur.execute('SELECT * FROM users')

if (cur.fetchall() is None) or cur.fetchall() == []:
    users = [
        ('user1','user1',0),
        ('user2','user2',0),
        ('admin','admin',1)]
    try:
        cur.executemany("INSERT INTO users VALUES (?,?,?)",users)
        con.commit()
    except:
        print('This users already in table users')

cur.execute('''CREATE TABLE IF NOT EXISTS balance
               (user_login TEXT PRIMARY KEY REFERENCES users(login),
               user_balance INTEGER) ''')

cur.execute('SELECT * FROM balance')
if (cur.fetchall() is None) or cur.fetchall() == []:
    balance = [
        ('user1',2000),
        ('user2',7000),
        ('admin',0)]

    try:
        cur.executemany("INSERT INTO balance VALUES (?,?)",balance)
        con.commit()
    except:
        print('This user already have balance')

cur.execute('''CREATE TABLE IF NOT EXISTS denominations
               (denom_name INTEGER NOT NULL PRIMARY KEY,
               denom_balance INTEGER NOT NULL)''')

cur.execute('SELECT * FROM denominations')
if (cur.fetchall() is None) or cur.fetchall() == []:
    denominations = [
        (10,0),
        (20,7),
        (50,10),
        (100,9),
        (200,10),
        (500,10),
        (1000,22)]

    try:
        cur.executemany("INSERT INTO denominations VALUES (?,?)",denominations)
        con.commit()
    except:
        print('This denomination was create')

cur.execute('''CREATE TABLE IF NOT EXISTS transactions
               (id_transact INTEGER PRIMARY KEY AUTOINCREMENT,
               user_login TEXT REFERENCES users(login),
               transaction_name TEXT,
               transaction_information TEXT)''')
con.commit()

m.start(con)


