''' Task 2
Write a script to print out a set containing all the
colours from color_list_1 which are not present in color_list_2.'''

color_list_1 = input("Enter colors for list 1: ")
color_list_2 = input("Enter colors for list 2: ")
color_list_1 = set(color_list_1.split(','))
color_list_2 = set(color_list_2.split(','))
print(color_list_1.difference(color_list_2))
