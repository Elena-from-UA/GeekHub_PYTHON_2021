''' Task 2 (список з блоками)'''

def func(file,count_symb):
    
    list_str = ''
    with open(file) as f:
        for i in f.readlines():
            list_str += i
            
        if (count_symb*3) > len(list_str):
            print('Length symb in file < input number')
        else:
            new_list = []
            new_list.append(list_str[0:count_symb])

            b = len(list_str) // 2
            centr = list_str[b]
            n = count_symb // 2
            if count_symb % 2 != 0:
                centr = list_str[b-n:b+n+1]
            else:
                centr = list_str[b-n:b+n]
        
            new_list.append(centr)
            new_list.append(list_str[-(count_symb):])

            print(new_list)
        
func('test1.txt',5)

