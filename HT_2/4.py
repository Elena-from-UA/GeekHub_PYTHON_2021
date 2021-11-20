''' Task 4
Написати скрипт, який об'єднає три словника в новий.
Початкові словники не повинні змінитись. Дані можна "захардкодити".'''


dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}

totalDict = {}
totalDict.update(dict_1)
totalDict.update(dict_2)
totalDict.update(dict_3)
print(totalDict)
