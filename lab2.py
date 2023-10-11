price = 2.99
quantity = 3
tax_rate = 7.5
subtotal = quantity * price
tax = tax_rate / 100 * subtotal
total = subtotal + tax
maseeg = f"Price of item: {price}$\n Quantity: {quantity}\n Tax rate: {tax_rate}%\n \n Subtotal: {subtotal}$\n Tax: {round(tax,2)}$\n Total: {round(total,2)}$"

print(maseeg)

