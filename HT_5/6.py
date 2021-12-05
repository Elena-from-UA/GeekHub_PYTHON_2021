''' Task 6
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
P.S. Повинен вертатись генератор.'''

def func_range(*args):     
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
        while start < stop:
            yield start
            start += step
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
        while start < stop:
            yield start
            start += step
    elif len(args) == 3:
        if args[2] > 0:
            start = args[0]
            stop = args[1]
            step = args[2]
            while start < stop:
                yield start
                start += step
        elif args[2] < 0:
            start = args[1]
            stop = args[0]
            step = args[2]
            while stop > start:
                yield stop
                stop -= step*(-1)
        else:
            raise ValueError('Step cannot to be equal zero')
    else:
        raise TypeError('Range expected at most 3 arguments')
               

for i in func_range(20,10,-1):
    print(i)
    
