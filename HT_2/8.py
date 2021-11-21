''' Task 8
Написати скрипт, який отримує від користувача позитивне ціле число
і створює словник, з ключами від 0 до введеного числа,
а значення для цих ключів - це квадрат ключа.'''

userIntNum = int(input('Enter integer positive number: '))

if userIntNum < 0:
    print('Wrong answer!')

userDict = {}
for i in range(userIntNum + 1):
    userDict[i] = i*i

print(userDict)
