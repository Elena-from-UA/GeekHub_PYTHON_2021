''' Task 1
Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову,
яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.'''

user_num = int(input('Enter number: '))

for i in range(user_num):
    if i % 17 != 0:
        continue
    print(i)
        
