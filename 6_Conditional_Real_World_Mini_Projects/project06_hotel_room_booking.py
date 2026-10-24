# Mini Project 6: Hotel Room Booking System
guest = input("Guest name: ")
room = input("Room type (Standard/Deluxe/Suite): ").strip().title()
nights = int(input("Number of nights: "))

if nights <= 0:
    print("Number of nights must be greater than 0")
elif room != "Standard" and room != "Deluxe" and room != "Suite":
    print("Error: invalid room type")
else:
    if room == "Standard":
        rate = 2000
    elif room == "Deluxe":
        rate = 3500
    else:
        rate = 6000

    room_charge = rate * nights

    if nights >= 10:
        disc_percent = 20
    elif nights >= 5:
        disc_percent = 10
    else:
        disc_percent = 0

    discount = room_charge * disc_percent / 100
    final_amount = room_charge - discount

    print("\n------ BOOKING SUMMARY ------")
    print("Guest name      :", guest)
    print("Room type       :", room)
    print("Number of nights:", nights)
    print("Room charge     : Rs.", room_charge)
    print("Discount        : Rs.", discount, "(" + str(disc_percent) + "%)")
    print("Final amount    : Rs.", final_amount)
