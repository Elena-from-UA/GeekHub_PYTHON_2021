''' Task 3
Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте, и False - якщо ні.'''

def is_prime(num):
    if 0 <= num <= 1000:
        d = 2
        while d * d <= num and num % d != 0:
            d += 1
        return d * d > num
    else:
        print('Number is not in range')

print(is_prime(59))
