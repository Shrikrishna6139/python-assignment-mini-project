# Mini Project 4: Shopping Cart Total
n = int(input("Number of products: "))
subtotal = 0

for i in range(1, n + 1):
    print("\nProduct", i)
    price = float(input("  Price: Rs. "))
    qty = int(input("  Quantity: "))

    # reject negative values
    while price < 0 or qty < 0:
        print("  Price and quantity cannot be negative. Re-enter.")
        price = float(input("  Price: Rs. "))
        qty = int(input("  Quantity: "))

    item_total = price * qty
    print("  Item subtotal: Rs.", item_total)
    subtotal += item_total

# 10% discount for Rs.3000 and above
if subtotal >= 3000:
    discount = subtotal * 10 / 100
else:
    discount = 0

after_discount = subtotal - discount

# delivery free if discounted amount is Rs.1500 or more
if after_discount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = after_discount + delivery

print("\n------ BILL ------")
print("Subtotal        : Rs.", subtotal)
print("Discount        : Rs.", discount)
print("Delivery charge : Rs.", delivery)
print("Final payable   : Rs.", final_amount)
