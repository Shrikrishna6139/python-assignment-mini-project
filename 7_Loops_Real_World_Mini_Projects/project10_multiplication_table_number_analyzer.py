# Mini Project 10: Multiplication Table and Number Analyzer
n = int(input("Enter a positive integer for the table: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    print("\nMultiplication table of", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

    start = int(input("\nEnter start of range: "))
    end = int(input("Enter end of range: "))

    if start > end:
        print("Invalid range: start cannot be greater than end")
    else:
        even = 0
        odd = 0
        total = 0

        for num in range(start, end + 1):
            total += num
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        print("\n------ RANGE ANALYSIS ------")
        print("Even count   :", even)
        print("Odd count    :", odd)
        print("Sum of range :", total)
