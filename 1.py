price= 8.90
quantity = 5
tax_rate = 0.0075
subtotal = price*quantity


print(f"price=${price} ")
print(f"quantity=${quantity}")
print (f"tax_rate={tax_rate*100}%" )
print()

tax=round(subtotal*tax_rate,2)
total= tax+subtotal
print(f"subtotal=${subtotal}")
print(f"tax=${tax}")
print(f"total:$ {total}")
