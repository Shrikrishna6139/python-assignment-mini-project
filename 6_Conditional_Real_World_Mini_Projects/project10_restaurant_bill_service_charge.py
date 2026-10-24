# Mini Project 10: Restaurant Bill and Service Charge
name = input("Customer name: ")
bill = float(input("Food bill amount: "))
member = input("Membership (Yes/No): ").strip().lower()

if bill < 0:
    print("Invalid bill amount")
elif member != "yes" and member != "no":
    print("Membership must be Yes or No")
else:
    if bill >= 5000:
        rate = 15
    elif bill >= 3000:
        rate = 10
    elif bill >= 1000:
        rate = 5
    else:
        rate = 0

    if member == "yes":
        rate += 5

    discount = bill * rate / 100
    after_discount = bill - discount

    # service charge is added AFTER the discount
    service = after_discount * 5 / 100
    final_amount = after_discount + service

    print("\n------ RESTAURANT BILL ------")
    print("Customer name  :", name)
    print("Original bill  : Rs.", bill)
    print("Discount       : Rs.", discount, "(" + str(rate) + "%)")
    print("Service charge : Rs.", service)
    print("Final payable  : Rs.", final_amount)
    if final_amount >= 5000:
        print("Message        : Thank you for being a valued customer")
