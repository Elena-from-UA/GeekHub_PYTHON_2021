''' Task 5
5. Створіть за допомогою класів та продемонструйте свою
реалізацію шкільної бібліотеки(включіть фантазію).'''

class Library(object):

    def __init__(self,book,author,count):
        self.book = book
        self.author = author
        self.count = count

    def give_book(self):
        self.count = self.count - 1
        return self.count

    def get_book(self):
        self.count = self.count + 1
        return self.count
        
class Student(object):
    
    def __init__(self,student,form):
        self.student = student
        self.form = form
 
class Archive(object):

    def __init__(self,book,student):
        self.book = book
        self.student = student

    def inp_book(self):
        return f'Count this book = {self.book.get_book()}'
    
    def out_book(self):
        return f'Count this book = {self.book.give_book()}'


book_1 = Library('Code Da Vinci', 'Den Brown',10)
book_2 = Library('11/22/63', 'Stephen King',7)
student_1 = Student('Ivan  Pupkin','5A')
libr_archive_1 = Archive(book_1,student_1)

print(libr_archive_1.inp_book())
print(libr_archive_1.out_book())

libr_archive_2 = Archive(book_2,student_1)
print(libr_archive_2.out_book())
