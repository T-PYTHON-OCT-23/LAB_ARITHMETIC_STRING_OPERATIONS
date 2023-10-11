
apple_price = 10.95
apple_quantity = 6
tax_rate = 0.075

sub_total = apple_price*apple_quantity
tax = round(sub_total*tax_rate, 2)
total = sub_total+tax

print(f"Price of apple: ${apple_price}")
print(f"Quantity: {apple_quantity}")
print(f"Tax rate: {tax_rate*100}%")
print()
print(f"Subtotal: ${sub_total}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")


