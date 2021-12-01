''' Task 6
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
P.S. Повинен вертатись генератор.'''

def func_range(start,stop,step=1):
    i = start
    while i < stop:
        yield i
        i += step

for i in func_range(1,20,3):
    print(i)
    
