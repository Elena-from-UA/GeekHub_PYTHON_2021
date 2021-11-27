''' Task 5
Написати функцію < fibonacci >,яка приймає один аргумент і виводить всі числа Фібоначчі,
що не перевищують його.'''

def fibonacci(num):
    list_fb = []    
    fb_1 = fb_2 = 1
    while fb_1 <= num:
        list_fb.append(fb_1)
        fb_1, fb_2 = fb_2, fb_1 + fb_2 
    print(list_fb)
    
fibonacci(30)
