childs_meal = float(input("What is the price of a child's meal?: "))
adults_meal = float(input("What is the price of an adult's meal?: "))
children_amount = int(input('How many children are there?: '))
adult_amount = int(input('How many adults are there?: '))
tax_rate = float(input('What is the tax rate?: '))
total_pre_tax = childs_meal * children_amount + adults_meal * adult_amount
sales_tax = total_pre_tax * tax_rate / 100
total = sales_tax + total_pre_tax

multiline_string = f'''
Subtotal: {total_pre_tax}
Sales tax: {round(sales_tax, 2)}
Total: {(round(total, 2))}
'''
print(multiline_string)

paymment_amount = float(input('What is the payment amount?: '))
print(f'Change {round(paymment_amount - total, 2)}')

sign = input('Please sign your name here: ')
print(f'Thanks for coming {sign}.')