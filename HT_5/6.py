''' Task 6
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
P.S. Повинен вертатись генератор.'''

def func_range(start,stop):
    i = start
    while i < stop:
        yield i
        i += 1

for i in func_range(1,9):
    print(i)
    
