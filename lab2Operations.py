price = 2.99
quantity = 3
tax_rate = 0.075


itemData = f"Price of item: ${str(price)} \nQuantity: {str(quantity)} \nTax rate: {str(tax_rate *100) }%\n"
print(itemData)

subtotal = price * quantity 
tax = subtotal * 0.075
total = subtotal + tax
output = f"Subtotal: ${str(round(subtotal, 2))}\nTax: ${str(round(tax, 2))} \nTotal: ${str(round(total, 2))} "
print(output)