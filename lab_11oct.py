# LAB_ARITHMETIC_STRING_OPERATIONS


#You are a cashier at a grocery store. Write a Python program to calculate the total cost of a customer's purchase, including tax.

#1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 3.34
#2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = 4
#3. Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = 0.075
#4. Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity
#5. Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = tax_rate * subtotal
#6. Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = tax + subtotal
#7. Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print(f"Price of item: {price} SR \nQuantity: {quantity} \nTax rate: {tax_rate*100}% \n\nSubtotal: {subtotal} SR \nTax: {tax} SR \nTotal: {total} SR")

