

print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = None

while item != "quit":
    item = input("Item: ")
    if item != "quit":
        shopping_list.append(item)

print ("The shopping list is: ")
for item in shopping_list:
    print(item)

print()
print("The shopping list with indexes is: ")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")
print()

index = int(input("Which is the item you would like to change?: "))
new_item = input("what is the new item?: ")
print()

shopping_list[index] = new_item

print("The shopping list with indexes is:")
for index in range(len(shopping_list)):
    item = shopping_list[index]
    print(f"{index}. {item}")
