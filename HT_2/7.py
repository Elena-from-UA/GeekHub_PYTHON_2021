''' Task 7
Написати скрипт, який отримає максимальне і мінімальне значення із словника.
Дані захардкодити.'''

dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
newList = list(dict_1.values())
print('MIN: ', min(newList))
print('MAX: ', max(newList))
