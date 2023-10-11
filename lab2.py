PriceOfItem = 2.99
output1 = f"Price = {PriceOfItem} $" 
print(output1)

QuantityOfItem = 3
output2 = f"Quantity= {QuantityOfItem} " 
print(output2)

tax_rate= 0.075
output3 = "Tax_rate= {} % " .format(tax_rate*100)
print(output3)
Subtotal = PriceOfItem * QuantityOfItem 
print("Subtotal= {}  $ ".format(Subtotal))

Tax  = round(Subtotal * tax_rate,2)
print(f"Tax= {Tax} $")

Total_Cost = round(Subtotal + Tax,2)
print(f"Total Cost={Total_Cost} $")