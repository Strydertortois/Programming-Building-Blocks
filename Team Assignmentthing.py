import math


length_square = int(input('What is the length of a side of the square? ') )
area_square = length_square ** 2 
print (f'The area of the square is: {area_square}')

length_rectangle = int(input('What is the length of the rectangle? '))
width_rectangle = int(input('What is the width of the rectangle? '))
area_rectangle = length_rectangle * width_rectangle
print (f'The area of the rectangle is: {area_rectangle}')

radius_circle = int(input('What is the radius of the circle? '))
area_circle = (radius_circle * math.pi)
print(f'The area of the circle is: {area_circle}')

