

names = ["bob", "jim", "john", "Jane", "jill", "linda"]
ages = [34, 22 ,39, 47, 59, 68]


names[2] = "tommy"
ages[2] = 10
names[5] = "andy"
ages[5] = 78
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

print()
print()

names.pop(4)
ages.pop(4)
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")