""" Task 2
Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної."""

import requests
import datetime
import time

def format_date(date):
    try:
        datetime_obj = datetime.datetime.strptime(date, '%d.%m.%Y')
    except:
        print('wrong date')
    else:
        return datetime_obj

def check_exchange_rate(currency):
    
    date = datetime.datetime.today()
    date = date.strftime("%d.%m.%Y")
    param = {'date':date}
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&'
    res = requests.get(url,param)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    dict_exchange = data.get('exchangeRate')
    currency_list = []
    for i in data.get('exchangeRate'):
        currency_list.append(i.get('currency'))
    if currency not in currency_list:
        return False
    else:
        return True

def get_exchange_rate(currency,date):
    param = {'date':date}
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&'
    res = requests.get(url,param)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    dict_exchange = data.get('exchangeRate')
    for i in data.get('exchangeRate'):
        if i.get('currency') == currency:
            return i.get("saleRateNB")
    
def main(currency,date):
    
    date = format_date(date)
    if date > datetime.datetime.today():
        print('date cannot be greater than current')
    else:
        new_date = date.strftime("%d.%m.%Y")
        check_currency = check_exchange_rate(currency)
        if check_currency == False:
            print('Wrong currency')
        else:
            delta_days = datetime.datetime.today() - date
            days = delta_days.days
            print(f'Currency: {currency}\n')
            while days >= 0:
                time.sleep(0.5)
                past_date = datetime.datetime.today() - datetime.timedelta(days)
                past_date = past_date.strftime("%d.%m.%Y")
                print(f'Date: {past_date}')
                NBU = get_exchange_rate(currency,past_date)
                yesterday = datetime.datetime.today() - datetime.timedelta(days+1)
                yesterday = yesterday.strftime("%d.%m.%Y")
                NBU_last_day = get_exchange_rate(currency,yesterday)
                result = NBU - NBU_last_day
                print(f'NBU: {NBU}          {result}\n')
                days -= 1
    
print(main(input('Enter currency (examp."USD"): '),input('Enter date (examp."15.12.2021"): ')))
