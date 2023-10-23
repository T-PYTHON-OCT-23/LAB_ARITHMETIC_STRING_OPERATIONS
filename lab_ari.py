# Define the variables
price = 2.99
quantity = 3
tax_rate = 0.075  # 7.5%

# Calculate the subtotal
subtotal = price * quantity

# Calculate the tax
tax = subtotal * tax_rate

# Calculate the total cost
total = subtotal + tax

# print 
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}% \n")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
