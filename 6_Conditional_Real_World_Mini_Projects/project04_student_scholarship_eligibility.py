# Mini Project 4: Student Scholarship Eligibility
name = input("Student name: ")
percentage = float(input("Percentage: "))
income = float(input("Annual family income: "))
attendance = float(input("Attendance percentage: "))

print("\n------ SCHOLARSHIP RESULT ------")
print("Student name:", name)

if percentage >= 75 and income <= 400000 and attendance >= 75:
    print("Eligibility status : Eligible")
    if percentage >= 90:
        print("Scholarship category: Full Scholarship")
    else:
        print("Scholarship category: Partial Scholarship")
else:
    print("Eligibility status : Not Eligible")
    print("Scholarship category: None")
    # explain every failed condition
    if percentage < 75:
        print("Reason: percentage is below 75%")
    if income > 400000:
        print("Reason: family income is above Rs.4,00,000")
    if attendance < 75:
        print("Reason: attendance is below 75%")
