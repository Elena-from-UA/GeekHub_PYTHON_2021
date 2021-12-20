""" Task 3
Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
конвертацію введеної суми з однієї валюти в іншу."""

import requests
import datetime
 
def get_exchange_rate(currency):
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
        print('Wrong currency')
        return False
    else:    
        for i in data.get('exchangeRate'):
            if i.get('currency') == currency:
                return i.get("saleRateNB")

def main(inp_currency,out_currency,sum_inp):
    NBU_inp_currency = get_exchange_rate(inp_currency)
    NBU_out_currency = get_exchange_rate(out_currency)
    if (NBU_inp_currency != False) and (NBU_out_currency != False):
        result = (NBU_inp_currency * int(sum_inp)) / NBU_out_currency
        print(f'{sum_inp} {inp_currency} = {result} {out_currency}')

print(main(input('Enter currency: '),
           input('Enter convertation currency: '),
           input('Enter your sum: ')))

