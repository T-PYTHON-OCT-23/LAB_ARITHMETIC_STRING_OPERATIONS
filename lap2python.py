price = 2.99
quantity = 3
tax_rate = 0.075

subTotal = price*quantity
tax = round( subTotal*tax_rate, 2)
total_cos = subTotal+tax

print(f"price of itme : ${ price}")
                        
print(f"Quantity:$ {quantity}")
print(f"Tax rate: ${tax_rate*100}")
print(f"subtotal:${total_cos}")
print(f"Tax: $ {tax}")
print(f"Total: ${total_cos}")