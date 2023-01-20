



people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 1000
youngest_name = ''

for person in people:
    person_info = person.split()
    #print(person_info)
    age = int(person_info[1])
    name = person_info[0]
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f'{youngest_name} is the youngest person and is {youngest_age} years old')