''' Task 1
1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )'''

class Calc():
    """Class to perform mathematical operations."""
    
    last_result = None
    
    def summ(self,arg_1,arg_2):
        """Class method for sum 2 numbers"""
        
        self.last_result = arg_1 + arg_2
        return arg_1 + arg_2

    def subtr(self,arg_1,arg_2):
        """Class method for subtraction 2 numbers"""
        
        self.last_result = arg_1 - arg_2
        return arg_1 - arg_2

    def multip(self,arg_1,arg_2):
        """Class method for multiplication 2 numbers"""
        
        self.last_result = arg_1 * arg_2
        return arg_1 * arg_2

    def divis(self,arg_1,arg_2):
        """Class method for division 2 numbers"""
        
        try:
            arg_1 / arg_2
        except:
            return 0
        self.last_result = arg_1 / arg_2
        return arg_1 / arg_2


example = Calc()
print(f'last result = {example.last_result}')
print(f'Sum two numbers = {example.summ(10,5)}')
print(f'last result = {example.last_result}')
print(f'Division two numbers = {example.divis(10,5)}')
print(f'last result = {example.last_result}')

