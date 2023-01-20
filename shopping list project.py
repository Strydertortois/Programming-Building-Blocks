print()
print("Welcome to the Shopping Cart Program!")
print()

shopping_cart_items = []
item_prices = []
added_price = None
added_item = None
entered_action = 1
total = 0

while entered_action ==1 or entered_action ==2 or entered_action ==3 or entered_action ==4:
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    entered_action = int(input("Please enter an action: "))

    if entered_action == 1:
        added_item = input("What item would you like to add? ")
        added_price = float(input("What is the price of this item? "))
        print(f"'{added_item.capitalize()}' has been added to the cart.")
        print()
        shopping_cart_items.append(added_item)
        item_prices.append(added_price)

    if entered_action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart_items)):
            item = shopping_cart_items[i]
            item_price = item_prices[i]
            print(f"{i + 1}. {item.capitalize()} - ${item_price}")
        print()

    if entered_action == 3:
        for i in range(len(shopping_cart_items)):
            remove_item = int(input("Which item would you like to remove? (Number value) "))
            item = shopping_cart_items[i]
            print(f"{i + 1}. {item.capitalize()}")
            

        else:
            print('Sorry, that is not a valid item number.')

    if entered_action == 4:
        total = sum(item_prices)
        print(f"The total is: ${total:.2f}")
        print()
        
    if entered_action == 5:
        print("Thank you. Goodbye.")