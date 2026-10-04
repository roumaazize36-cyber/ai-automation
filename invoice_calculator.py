service_price = float(input("What is the service price (€)? "))
quantity = int(input("How many services? "))
discount = float(input("What is the discount percentage? "))
tax = float(input("What is the tax percentage? "))
subtotal = service_price * quantity
discount_amount = subtotal * (discount / 100)
after_discount = subtotal - discount_amount
tax_amount = after_discount * (tax / 100)
total = after_discount + tax_amount

print()
print(f"Subtotal: €{subtotal:,.2f}")
print(f"Discount: €{discount_amount:,.2f}")
print(f"Tax: €{tax_amount:,.2f}")
print(f"Final total: €{total:,.2f}") 