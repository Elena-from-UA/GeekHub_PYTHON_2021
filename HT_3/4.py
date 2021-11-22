''' Task 4
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат
та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3'''

def func_1(input_value):
    # кодування вхідного значення навпаки
    
    new_value = ''
    i = len(input_value) - 1
    while i >= 0:
        new_value = new_value + input_value[i]
        i = i - 1
    return new_value


def func_2(input_value):
    # кодування вхідного значення в бінарний код

    new_value = bin(input_value)
    return new_value


def func_3(input_value):
    # кодування вхідного значення в ASCII

    new_value = []
    for i in input_value:
        new_symb = ord(i)
        new_value.append(new_symb)
    return new_value
        

def func_4(value_1, value_2, value_3):
    # виведення даних з попередніх функцій

    result_for_func_1 = func_1(value_1)
    result_for_func_2 = func_2(value_2)
    result_for_func_3 = func_3(value_3)

    print(f'{value_1} is {result_for_func_1}')
    print(f'{value_2} is {result_for_func_2}')
    print(f'{value_3} is {result_for_func_3}')


func_4('hello', 100, 'python')
