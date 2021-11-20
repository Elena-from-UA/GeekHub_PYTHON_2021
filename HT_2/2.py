''' Task 2
Написати скрипт, який пройдеться по списку, який складається із кортежів,
і замінить для кожного кортежа останнє значення.
Список із кортежів можна захардкодити. Значення, на яке замінюється
останній елемент кортежа вводиться користувачем.
Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком).
Кількість елементів в кортежу повинна бути різна.'''

userElement = input("Enter element for list: ")
testList = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,), (10, 450)]
newList = []
for tupleInList in testList:
    convList = list(tupleInList)
    convList.pop()
    convList.append(userElement)
    tupleInList = tuple(convList)
    newList.append(tupleInList)
    
print(newList)
