''' Task 3
Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".'''

userList = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', [], (1,2,3)]
newList = []
for i in userList:
    if len(i) != 0:
        newList.append(i)
print(newList)
