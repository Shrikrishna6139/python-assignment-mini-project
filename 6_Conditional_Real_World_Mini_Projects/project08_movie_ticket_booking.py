# Mini Project 8: Movie Ticket Booking
name = input("Customer name: ")
age = int(input("Age: "))
show = input("Show type (Morning/Evening): ").strip().lower()
day = input("Day type (Weekday/Weekend): ").strip().lower()

if age < 0:
    print("Age cannot be negative")
elif show != "morning" and show != "evening":
    print("Invalid show type")
elif day != "weekday" and day != "weekend":
    print("Invalid day type")
else:
    base_price = 200
    discount = 0

    # age based discount (only one applies, children get priority)
    if age < 12:
        discount = base_price * 50 / 100
    elif age >= 60:
        discount = base_price * 30 / 100

    # morning show gives an extra Rs.30 off
    if show == "morning":
        discount = discount + 30

    surcharge = 0
    if day == "weekend":
        surcharge = 50

    final_price = base_price - discount + surcharge
    if final_price < 0:
        final_price = 0

    print("\n------ TICKET DETAILS ------")
    print("Customer name         :", name)
    print("Original ticket price : Rs.", base_price)
    print("Discount              : Rs.", discount)
    print("Weekend surcharge     : Rs.", surcharge)
    print("Final ticket price    : Rs.", final_price)
