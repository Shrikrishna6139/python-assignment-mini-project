# Mini Project 3: ATM Withdrawal System
name = input("Account holder name: ")
balance = float(input("Current balance: "))
amount = float(input("Withdrawal amount: "))

print("\n------ ATM TRANSACTION ------")
print("Account holder:", name)

if amount <= 0:
    print("Transaction status: Rejected")
    print("Reason: withdrawal amount must be greater than Rs.0")
elif amount > balance:
    print("Transaction status: Rejected")
    print("Reason: insufficient balance")
elif amount > 20000:
    print("Transaction status: Rejected")
    print("Reason: maximum limit per transaction is Rs.20,000")
else:
    balance = balance - amount
    print("Transaction status: Successful")
    print("Withdrawn amount  : Rs.", amount)
    print("Remaining balance : Rs.", balance)
    if balance < 1000:
        print("Low Balance Warning")
