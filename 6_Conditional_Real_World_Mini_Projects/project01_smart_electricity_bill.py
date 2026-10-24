# Mini Project 1: Smart Electricity Bill Calculator
name = input("Customer name: ")
units = float(input("Units consumed: "))

if units < 0:
    print("Invalid input: units cannot be negative")
else:
    # slab-wise energy charge
    if units <= 100:
        energy = units * 3
    elif units <= 200:
        energy = 100 * 3 + (units - 100) * 5
    else:
        energy = 100 * 3 + 100 * 5 + (units - 200) * 7

    service = 150
    final_bill = energy + service

    print("\n------ ELECTRICITY BILL ------")
    print("Customer name  :", name)
    print("Units consumed :", units)
    print("Energy charge  : Rs.", energy)
    print("Service charge : Rs.", service)
    print("Final bill     : Rs.", final_bill)

    if final_bill > 5000:
        print("Usage message  : High Usage Bill")
    else:
        print("Usage message  : Normal usage")
