

number = int(input('Please input a positive number (>= 0): '))

while number < 0:
    print(f'Sorry: {number} is negative.  Please try again')
    number = int(input('Please input a positive number (>= 0): '))

print(f'{number} is a positive number.')


have_candy = input('May I have a piece of Candy? ')

while have_candy.lower() != 'yes':
    have_candy = input('May I have a piece of Candy? ')

print('Thank You')
