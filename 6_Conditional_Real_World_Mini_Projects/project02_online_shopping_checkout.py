# Mini Project 2: Online Shopping Checkout
name = input("Customer name: ")
amount = float(input("Purchase amount: "))
ctype = input("Customer type (Regular/Premium): ").strip().lower()

if amount < 0:
    print("Invalid purchase amount")
elif ctype != "regular" and ctype != "premium":
    print("Invalid customer type")
else:
    if amount >= 5000:
        rate = 20
    elif amount >= 3000:
        rate = 10
    elif amount >= 1000:
        rate = 5
    else:
        rate = 0

    # premium customers get an extra 5%
    if ctype == "premium":
        rate += 5

    discount = amount * rate / 100
    after_discount = amount - discount

    # delivery is free for Rs.2000 and above
    if after_discount >= 2000:
        delivery = 0
    else:
        delivery = 100

    final_amount = after_discount + delivery

    print("\n------ CHECKOUT SUMMARY ------")
    print("Customer name  :", name)
    print("Discount       : Rs.", discount, "(" + str(rate) + "%)")
    print("Delivery charge: Rs.", delivery)
    print("Payable amount : Rs.", final_amount)
