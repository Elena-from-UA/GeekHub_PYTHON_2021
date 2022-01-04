''' Task 6
6. Створіть клас в якому буде атребут який буде рахувати
кількість створених екземплярів класів.'''

class Books(object):

    count = 0

    def __init__(self,name,author):
        self.name = name
        self.author = author
        Books.count += 1

book_1 = Books('Code Da Vinci', 'Den Brown')
book_2 = Books('11/22/63', 'Stephen King')
book_3 = Books('Martin Eden', 'Jack London')

print(Books.count)
