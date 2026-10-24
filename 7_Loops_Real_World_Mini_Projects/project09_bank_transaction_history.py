# Mini Project 9: Bank Transaction History
balance = float(input("Opening balance: Rs. "))
n = int(input("Number of transactions: "))

deposits = 0
withdrawals_ok = 0
withdrawals_rejected = 0

for i in range(1, n + 1):
    print("\nTransaction", i)
    t_type = input("  Type (deposit/withdraw): ").strip().lower()
    amount = float(input("  Amount: Rs. "))

    if amount <= 0:
        print("  Status: Rejected (amount must be positive)")
    elif t_type == "deposit":
        balance += amount
        deposits += 1
        print("  Status: Deposit successful")
    elif t_type == "withdraw":
        if amount <= balance:
            balance -= amount
            withdrawals_ok += 1
            print("  Status: Withdrawal successful")
        else:
            withdrawals_rejected += 1
            print("  Status: Withdrawal rejected (insufficient funds)")
    else:
        print("  Status: Invalid transaction type")

print("\n------ ACCOUNT SUMMARY ------")
print("Final balance             : Rs.", balance)
print("Deposit count             :", deposits)
print("Successful withdrawals    :", withdrawals_ok)
print("Rejected withdrawals      :", withdrawals_rejected)
if balance < 1000:
    print("Warning: balance is below Rs.1,000")
