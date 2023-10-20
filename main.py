# LAB_ARITHMETIC_STRING_OPERATIONS


price:float = 2.99
quantity:int = 3
tax_rate:float = 0.075

subtotal = (price * quantity)
tax = round(subtotal * tax_rate , 2 )
total = (subtotal + tax)


print(f"Price of item : $ {price}")
print(f"Quantity :  {quantity}")
print(f"Tax rate :  {tax_rate*100}%")
print("-"*18)

print(f"Subtotal : $ {subtotal}")
print(f"Tax : $ {tax}")
print(f"Total : $ {total}")








