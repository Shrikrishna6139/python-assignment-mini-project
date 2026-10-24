# Mini Project 5: Employee Performance Bonus
name = input("Employee name: ")
salary = float(input("Monthly salary: "))
experience = float(input("Years of experience: "))
rating = int(input("Performance rating (1-5): "))

if rating < 1 or rating > 5:
    print("Invalid rating. It must be between 1 and 5")
else:
    if experience >= 10 and rating >= 4:
        percent = 20
    elif experience >= 5 and rating >= 4:
        percent = 15
    elif experience >= 2 and rating >= 3:
        percent = 10
    else:
        percent = 0      # includes rating below 3

    bonus = salary * percent / 100
    final_salary = salary + bonus

    print("\n------ BONUS REPORT ------")
    print("Employee name   :", name)
    print("Bonus percentage:", percent, "%")
    print("Bonus amount    : Rs.", bonus)
    print("Final salary    : Rs.", final_salary)
    if rating == 5:
        print("Message         : Excellent Performer")
    elif rating >= 3:
        print("Message         : Good performance")
    else:
        print("Message         : Needs improvement")
