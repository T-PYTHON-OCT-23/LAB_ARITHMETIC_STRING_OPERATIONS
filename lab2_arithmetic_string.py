price = 2.99
quantity = 3
tax_rate = 0.075
tax_rate = float(0.075)
y = (tax_rate * 100)

subtotal = price*quantity
the_tax = round(subtotal*tax_rate,2)
total = round(subtotal + the_tax,2) 
print("Price of item:" + "$" +str(price))
print("Quantity:" + str(quantity))
print("Tax rate:"+ str(y)+"%")
print()
print("Subtotal:"+ "$" + str(subtotal))
print("Tax:" + "$" + str(the_tax))
print("Total:"+ "$" + str(total))
