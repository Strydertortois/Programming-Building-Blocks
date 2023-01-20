

age_1 = int(input('What is the age of the first rider?: '))
height_1 = int(input('What is the height of the first rider?: '))
yes_no = input('Is there a second rider?: ')
if yes_no.lower() == 'no' and age_1 >= 18 and height_1 >= 62:
    print('Welcome to the ride! Please be safe and have fun!')
else:
    print('Sorry! You cannot ride!')
if yes_no.lower() == 'yes':
    age_2 = int(input('What is the age of the second rider?: '))
    height_2 = int(input('What is the height of the second rider?: '))
    if 




