''' Task 7
Написати функцію, яка приймає на вхід список
і підраховує кількість однакових елементів у ньому.'''

def func(list_num):
    new_dict = {}
    for i in list_num:
        new_dict.update({i:list_num.count(i)})
    print(new_dict)

func([1,3,5,5,7,7,'h','b','b'])
