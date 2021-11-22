''' Task 3
Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде
повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)'''

def season(num_month):
    dict_season = {(1,2,12):'Winter', (3,4,5):'Spring', (6,7,8):'Summer', (9,10,11):'Autumn'}
    for key in dict_season:
        for i in key:
            if i == num_month:
                print(dict_season.get(key))

season(11)
