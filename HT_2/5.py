''' Task 5
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями
(дублікати значень - видалити). Словник для роботи захардкодити свій.'''

userDict = {'1':'test', '2':'python', '3':'hometask', '4':'test', '5':'hometask'}
values = set()
newDict = {}

for k,v in userDict.items():
    if v not in values:
        newDict.update({k: v})
        values.add(v)
    
print(newDict)
