''' Task 3
3. Напишіть програму, де клас «геометричні фігури» (figure)
містить властивість color з початковим значенням white і
метод для зміни кольору фігури, а його підкласи «овал» (oval)
і «квадрат» (square) містять методи __init__ для завдання початкових
розмірів об'єктів при їх створенні.'''

class Figure(object):
    color = 'white'

    def change_color(self,color):
        self.color = color

class Oval(Figure):

    def __init__(self,small_radius,big_radius):
        self.small_radius = small_radius
        self.big_radius = big_radius

class Square(Figure):

    def __init__(self,side):
        self.side = side
        
figure_1 = Figure()
print(figure_1.color)
figure_1.color = 'red'
print(figure_1.color)
figure_1.change_color('yellow')
print(figure_1.color)

figure_2 = Oval(5,10)
print(figure_2.small_radius,figure_2.big_radius)

figure_3 = Square(7)
figure_3.color = 'black'
print(figure_3.side)
print(figure_3.color)
