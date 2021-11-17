'''  Task 1
Write a script which accepts a sequence of comma-separated
numbers from user and generate a list and a tuple with those numbers.'''

numSequence = input("Enter some numbers with symbol ',' : ")
list = numSequence.split(",")
tuple = tuple(list)
print('List: ',list)
print('Tuple: ',tuple)
