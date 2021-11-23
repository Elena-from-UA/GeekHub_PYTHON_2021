''' Task 7
Ну і традиційно -> калькулятор :)
повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!'''

def calc(arg_1, operation, arg_2):
    if operation == '+':
        print(arg_1 + arg_2)
    elif operation == '-':
        print(arg_1 - arg_2)
    elif operation == '*':
        print(arg_1 * arg_2)
    elif operation == '/':
        if arg_2 == 0:
            print('You can not divide by zero')
        else:
            print(arg_1 / arg_2)
    else:
        print('incorrect values')

calc(10, '/' ,0)
