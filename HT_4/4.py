''' Task 4
Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.'''

def prime_list(start,end):
    list_simple_num = []
    for i in range(start,end+1):
        d = 2
        while d * d <= i and i % d != 0:
            d += 1
        if d * d > i:
            list_simple_num.append(i)
    return print(list_simple_num)

prime_list(1,31)
