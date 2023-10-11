price = 2.99
quantity = 3
tax_rate = 7.5

print("Price of item: $" + str(price))
print("Quantity: " + str(quantity))
print("Tax rate: " + str(tax_rate) + "% \n" )

subtotal = price * quantity 
tax = subtotal * 0.075
total = subtotal + tax
output = f"Subtotal: ${str(round(subtotal, 2))}\nTax: ${str(round(tax, 2))} \nTotal: ${str(round(total, 2))} "
print(output)