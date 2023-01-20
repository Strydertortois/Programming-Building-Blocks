

numbers = [4,5,6,7,8,9,10,11,12,13,14]

print(numbers)
numbers[4] = 99999
numbers[10] = 1010
print(numbers)

numbers.pop(4)

print(numbers)

for index in range(len(numbers)):
    number = numbers[index]
    if number == 8:
        numbers[index] = 99999
        number = numbers[index]
    print(f'{index}. {number}')

#numbers = [4,5,6,7,8,9,10,11,12,13,14]

#for index in range(len(numbers)):
  #  numbers.pop(0)
  #  print(numbers)