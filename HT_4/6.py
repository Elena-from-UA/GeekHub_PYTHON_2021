''' Task 6
Вводиться число. Якщо це число додатне, знайти його квадрат,
якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.'''

def check_num(num):
    if num > 0:
        print(f'Square of {num} =', num ** 2)
    elif num < 0:
        print(f'New value of {num} =', num + 100)
    else:
        print(num)

check_num(10)
