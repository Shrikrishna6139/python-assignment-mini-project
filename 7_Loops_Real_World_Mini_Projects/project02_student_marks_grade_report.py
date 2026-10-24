# Mini Project 2: Student Marks and Grade Report
n = int(input("Number of students: "))

total_marks = 0
passed = 0
failed = 0

for i in range(1, n + 1):
    name = input("\nStudent " + str(i) + " name: ")
    marks = float(input("Marks out of 100: "))

    # reject marks outside 0-100 and ask again
    while marks < 0 or marks > 100:
        print("Invalid marks! Enter between 0 and 100")
        marks = float(input("Marks out of 100: "))

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    if grade == "Fail":
        failed += 1
    else:
        passed += 1

    total_marks += marks
    print(name, "-> Grade:", grade)

print("\n------ CLASS SUMMARY ------")
if n > 0:
    print("Class average :", round(total_marks / n, 2))
print("Pass count    :", passed)
print("Fail count    :", failed)
