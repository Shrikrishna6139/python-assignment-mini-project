# Mini Project 7: Mobile Data Plan Bill
name = input("Customer name: ")
plan = input("Plan type (Basic/Standard/Premium): ").strip().title()
extra_gb = float(input("Extra data used in GB: "))

if extra_gb < 0:
    print("Invalid input: data usage cannot be negative")
elif plan != "Basic" and plan != "Standard" and plan != "Premium":
    print("Invalid plan type")
else:
    if plan == "Basic":
        base = 299
        included = 10
    elif plan == "Standard":
        base = 499
        included = 25
    else:
        base = 799
        included = 50

    extra_charge = extra_gb * 20

    # surcharge applies if extra data goes beyond 10 GB
    if extra_gb > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base + extra_charge + surcharge

    print("\n------ MOBILE BILL ------")
    print("Customer name     :", name)
    print("Plan type         :", plan, "(includes", included, "GB)")
    print("Base plan charge  : Rs.", base)
    print("Extra data charge : Rs.", extra_charge)
    print("Surcharge         : Rs.", surcharge)
    print("Final bill        : Rs.", final_bill)
