''' Task 2
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.'''

class Person(object):
    """Class for information about Person"""
    
    def __init__(self,**kwargs):
        self.age = kwargs.get('age')
        self.name = kwargs.get('name')

    def show_age(self):
        """Class method for show age person"""
        
        return self.age

    def print_name(self):
        """Class method for print name person"""
        
        return self.name

    def show_all_information(self):
        """Class method for show all information about person"""
        
        return vars(self)
        

person_1 = Person(age=20, name='Ivo Bobul')
person_1.profession = 'singer'
print(person_1.show_all_information())

person_2 = Person(age=25, name='Stepan Bandera')
person_2.profession = 'politician'
print(person_2.show_all_information())

