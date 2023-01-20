

import math
from turtle import width


def area_of_square(side):
    return side * side

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    return math.pi * radius * radius


shape = ''

while shape != 'quit':
    shape = input('What shape would you like to calculate? (square, rectangle, circle): ')

    if shape == 'square':
        side = float(input('What is the length of the square?: '))
        area = area_of_square(side)
        print(f'The area of your square is {area}')
    
    if shape == 'rectangle':
        length = float(input('What is the length: '))
        width = float(input('What is the width: '))
        area = area_of_rectangle(length, width)
        print(f'The area of your rectangle is {area}')

    if shape == 'circle':
        radius = float(input('What is the radius: '))
        area = area_of_circle(radius)
        print(f'The area of your circle is {area}')


