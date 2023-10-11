
price = 2.99

quantity = 3

tax_rate = 7.5

subtotal = price * quantity

tax = subtotal * tax_rate/100


total= subtotal + tax
total=round(total,2)
tax=round(tax,2)

print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")



