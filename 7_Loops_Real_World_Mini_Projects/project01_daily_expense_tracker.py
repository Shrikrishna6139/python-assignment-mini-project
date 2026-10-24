# Mini Project 1: Daily Expense Tracker
days = int(input("Number of days: "))

if days <= 0:
    print("Number of days must be at least 1")
else:
    total = 0
    highest = 0

    for day in range(1, days + 1):
        expense = float(input("Expense for day " + str(day) + ": Rs. "))
        while expense < 0:
            expense = float(input("Expense cannot be negative. Re-enter: Rs. "))
        total += expense
        if expense > highest:
            highest = expense

    average = total / days

    print("\n------ EXPENSE SUMMARY ------")
    print("Total expense          : Rs.", total)
    print("Average daily expense  : Rs.", round(average, 2))
    print("Highest daily expense  : Rs.", highest)
    if total > 5000:
        print("Budget status          : Budget Alert")
    else:
        print("Budget status          : Within budget")
