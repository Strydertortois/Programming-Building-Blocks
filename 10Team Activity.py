

names = []
balances = []
name = None

while name != "quit":
    name = input("What is the name of the account?: ")

    if name != "quit":
        balance = float(input("What is the balance: "))
        
        names.append(name)
        balances.append(balance)  

total = 0 
print("account info: ")
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")

total += balances[i]
average = total / len(balances)
print()
print()
print(f"Total: ${total}")
print(f"Average: ${average}")








