price = 2.99 
print("Price of item:$ "+str(price))
quantity = 3
print("Quantity :$ "+str(quantity))
tax_rate = 0.075
print("Tax rate :% "+str(tax_rate*100))
subtotal = price*quantity
tax = subtotal*tax_rate
total = subtotal+tax
subtotal = round (subtotal,2)
tax= round(tax,2)
total=round(total,2)

print(f"subtotal:{subtotal}")
print(f"tax $: {tax}")
print(f"Total $: {total}")
