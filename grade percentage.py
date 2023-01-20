grade = int(input('What is your percentage?: '))

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print()
print(f'Your letter grade is {letter_grade}')

if grade >= 70:
    print('Congrats! You passed the class!')
else:
    print('You failed. Better luck next time!')

sign = ""

last_number = grade % 10

if last_number >= 7:
    sign = "+"
    


