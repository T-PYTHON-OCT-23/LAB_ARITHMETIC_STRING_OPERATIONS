
price=2.99
guantity=3
tax_rate=0.075

subtotal=price*guantity
tax=round(subtotal*tax_rate,2)
total=subtotal+tax

print('Price of item: $',price)
print('Quantity: {}'.format(guantity))
print(F'Tax rate: {tax_rate*100}')

print('Subtotal: $',subtotal)
print('Tax: $',tax)
print('Total: $',total)


