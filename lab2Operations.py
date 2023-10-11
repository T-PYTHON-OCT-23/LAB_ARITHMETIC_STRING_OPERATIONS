price = 2.99
quantity = 3
tax_rate = 7.5

print("Price of item: $" + str(price))
print("Quantity: " + str(quantity))
print("Tax rate: " + str(tax_rate) + "% \n" )
subtotal = price * quantity 
print("Subtotal: $" + str(round(subtotal, 2)))

tax = subtotal * 0.075
print("Tax: $" + str(round(tax, 2)))


total = subtotal + tax
print("Total: $" + str(round(total, 2)))
