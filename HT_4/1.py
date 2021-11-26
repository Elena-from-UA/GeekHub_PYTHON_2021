''' Task 1
 Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
 і вертатиме 3 значення (кортеж):
 периметр квадрата, площа квадрата та його діагональ.'''

import math

def square(side):
    perimeter = 4 * side
    area = side * side
    diagonal = math.sqrt(2 * (side ** 2))
    result = (perimeter, area, diagonal)
    return print(result)

square(5)
