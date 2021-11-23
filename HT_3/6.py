''' Task 6
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя'''

def func(string):
    str_len = len(string)
    
    if 30 <= str_len <= 50:
        print(f'Length string = {str_len}')
        count_num = count_symb = 0
        for i in string:
            if i.isdigit():
                count_num += 1
            elif i.isalpha():
                count_symb += 1
        print(f'Count numbers = {count_num},count letters = {count_symb}')

    elif str_len < 30:
        new_str = ''
        sum_num = 0
        for i in string:
            if i.isdigit():
                sum_num += int(i)
            elif i.isalpha():
                new_str += i
        print(f'Sum numbers = {sum_num}, string with only letters = {new_str}')
        
    elif str_len > 50:
        new_list = [string[i:i + 10] for i in range(0, str_len, 10)]
        print(f'List group by 10 symbols = {new_list}')
        
func('neroi4nr0c3n30irn03ienfghjklkjh')
