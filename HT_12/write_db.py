import sqlite3
import csv

def main():
    try:
        con = sqlite3.connect('information.db')
        cur = con.cursor()
        print("База данных успешно подключена к SQLite")

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    cur.execute('''CREATE TABLE IF NOT EXISTS quotes
                   (text_quotes TEXT NOT NULL PRIMARY KEY,
                   name_author TEXT NOT NULL)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS authors
                   (name TEXT NOT NULL PRIMARY KEY)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS about_authors
                   (name TEXT NOT NULL PRIMARY KEY REFERENCES authors(name),
                   date_born TEXT NOT NULL,
                   born_place TEXT NOT NULL,
                   description TEXT NOT NULL)''')
    con.commit()

    with open('quotes.csv','rt',encoding='utf-16') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT or IGNORE INTO quotes(text_quotes,name_author) VALUES (?,?)", row)
            
    with open('authors.csv','rt',encoding='utf-16') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT or IGNORE INTO authors(name) VALUES (?)", row)

    with open('about_authors.csv','rt',encoding='utf-16') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT or IGNORE INTO about_authors(name,date_born,born_place,description) VALUES (?,?,?,?)", row)
            
    con.commit()
