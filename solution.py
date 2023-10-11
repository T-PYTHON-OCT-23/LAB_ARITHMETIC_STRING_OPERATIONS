price = 2.99
quantity = 3
tax_rate = 0.075
subtotal = price *  quantity
tax = tax_rate * subtotal

total = subtotal + tax
print("Example output:")
print("```")
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print("```")
print(f"Subtotal: ${subtotal}")

print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("```")