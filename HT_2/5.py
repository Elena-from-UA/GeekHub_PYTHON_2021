''' Task 5
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями
(дублікати значень - видалити). Словник для роботи захардкодити свій.'''

userDict = {'1':'test', '2':[1,2,3], '3':'hometask', '4':'test', '5':'hometask', '6': (1,2,5)}}
values = set()
newDict = {}

for k,v in userDict.items():
    if type(v) == list:
            v = tuple(v)
    if v not in values:
        newDict.update({k: v})
        values.add(v)
    
print(newDict)
