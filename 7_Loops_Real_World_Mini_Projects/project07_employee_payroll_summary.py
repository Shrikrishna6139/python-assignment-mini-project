# Mini Project 7: Employee Payroll Summary
n = int(input("Number of employees: "))
total_net = 0

for i in range(1, n + 1):
    print("\nEmployee", i)
    name = input("  Name: ")
    basic = float(input("  Basic salary: Rs. "))
    overtime_hours = float(input("  Overtime hours: "))

    overtime_pay = overtime_hours * 200
    gross = basic + overtime_pay

    # 10% deduction for gross of Rs.50,000 or more, else 5%
    if gross >= 50000:
        deduction = gross * 10 / 100
    else:
        deduction = gross * 5 / 100

    net = gross - deduction
    total_net += net

    print("  ", name, "| Gross: Rs.", gross, "| Deduction: Rs.", deduction, "| Net: Rs.", net)

print("\n------ PAYROLL SUMMARY ------")
print("Employee count    :", n)
print("Total net payroll : Rs.", total_net)
