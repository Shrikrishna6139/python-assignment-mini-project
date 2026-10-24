# Mini Project 3: ATM PIN Verification
correct_pin = "4321"       # sample PIN stored in the program
max_attempts = 3
attempts = 0
granted = False

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        granted = True
        break
    else:
        print("Wrong PIN.", max_attempts - attempts, "attempt(s) left")

print("\n------ RESULT ------")
if granted:
    print("Access Granted")
else:
    print("Card Temporarily Locked")
print("Attempts used:", attempts)
