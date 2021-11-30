''' Task 7
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність
(рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності,
при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   >>>for elem in generator([1, 2, 3]):
   ...    print(elem)
   ...
   1
   2
   3
   1
   2
   3
   1
   .......'''
  

def generator(value):
    iterator = iter(value)
    while True:
        try:
            i = next(iterator)
        except:
            for i in value:
                print(i)

for elem in generator('qwerty'):
    print(elem)
