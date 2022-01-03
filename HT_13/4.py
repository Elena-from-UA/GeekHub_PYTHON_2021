''' Task 4
4. Видозмініть програму так,щоб метод __init__ мався в класі «геометричні фігури»
та приймав кольор фігури при створенні екземпляру,
а методи __init__ підкласів доповнювали його та додавали початкові розміри.'''

class Figure(object):

    def __init__(self,color='white'):
        self.color = color
        
    def change_color(self):
        self.color = color

class Oval(Figure):

    def __init__(self,color,small_radius,big_radius):
        Figure.__init__(self,color)
        self.small_radius = small_radius
        self.big_radius = big_radius
        

class Square(Figure):

    def __init__(self,color,side):
        Figure.__init__(self,color)
        self.side = side
        

        
figure_1 = Figure()
print(figure_1.color)
figure_1.color = 'red'
print(figure_1.color)

figure_2 = Oval('blue',5,10)
print(figure_2.small_radius,figure_2.big_radius,figure_2.color)

figure_3 = Square('black',7)
print(figure_3.side,figure_3.color)

