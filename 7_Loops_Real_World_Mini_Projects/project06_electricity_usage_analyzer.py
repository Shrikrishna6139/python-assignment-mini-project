# Mini Project 6: Electricity Usage Analyzer
days = int(input("Number of days: "))

if days <= 0:
    print("Number of days must be at least 1")
else:
    total = 0
    high_days = 0
    maximum = 0

    for d in range(1, days + 1):
        units = float(input("Units used on day " + str(d) + ": "))
        while units < 0:
            units = float(input("Units cannot be negative. Re-enter: "))

        total += units
        if units > 10:
            high_days += 1
        if units > maximum:
            maximum = units

    print("\n------ USAGE REPORT ------")
    print("Total units           :", total)
    print("Average usage         :", round(total / days, 2))
    print("Days with > 10 units  :", high_days)
    print("Maximum daily usage   :", maximum)
    if total > 300:
        print("Usage status          : High Usage")
    else:
        print("Usage status          : Normal")
