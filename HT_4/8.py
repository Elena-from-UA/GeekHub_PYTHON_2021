''' Task 8
Написати функцію, яка буде реалізувати логіку циклічного зсуву
елементів в списку. Тобто, функція приймає два аргументи: список і величину
зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]'''

def fnc(list_num, shift):
    i = 0
    if shift > 0:
        while i < shift:
            list_num.insert(0,list_num[-1])
            list_num.pop()
            i += 1 
        print(list_num)
    elif shift < 0:
        while i > shift:
            list_num.append(list_num[0])
            list_num.remove(list_num[0])
            i -= 1
        print(list_num)
    else:
        print(list_num)
        
fnc([1,2,3,4,5,6,7,8,9,10], 4)
