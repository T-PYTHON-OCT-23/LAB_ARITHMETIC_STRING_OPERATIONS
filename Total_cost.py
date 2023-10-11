#the cost of the item the customer is purchasing
price = 2.99
print(f"Price of item: ${price}")
#the number of items the customer is purchasing
quantity = 3
print(f"Quantity: {quantity}")
#the tax rate in your area
tax_rate = 7.5
print(f"Tax rate: {tax_rate} %")
#multiplying the price by the quantity
subtotal = price * quantity 
#multiplying the subtotal by the tax rate
tax = subtotal * (tax_rate / 100)
#Calculate the total cost by adding the subtotal and the tax
total = subtotal + tax
#Print the subtotal, tax, and total costs, formatted as currency
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${round(tax , 2)}")
print(f"Total: ${round(total , 2)}")