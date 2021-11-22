''' Task 2
Користувачем вводиться початковий і кінцевий рік. Створити цикл,
який виведе всі високосні роки в цьому проміжку (границі включно).'''

start_year = int(input('Enter start year: '))
end_year = int(input('Enter end year: '))

for i in range(start_year,end_year + 1):
    if i % 400 == 0:
        print(i)
    elif (i % 100 != 0) and (i % 4 == 0):
        print(i)
    else:
        continue
