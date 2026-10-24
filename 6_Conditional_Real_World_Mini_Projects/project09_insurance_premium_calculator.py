# Mini Project 9: Insurance Premium Calculator
name = input("Customer name: ")
age = int(input("Age: "))
risk = input("Occupation risk (Low/Medium/High): ").strip().title()
smoker = input("Smoker (Yes/No): ").strip().lower()

print("\n------ INSURANCE QUOTE ------")
print("Customer name:", name)

if age < 18:
    print("Eligibility  : Not eligible (age is below 18)")
elif risk not in ("Low", "Medium", "High") or smoker not in ("yes", "no"):
    print("Invalid occupation risk or smoker value")
else:
    print("Eligibility  : Eligible")

    base = 10000
    extra = 0

    if age > 50:
        extra += 5000
    if risk == "High":
        extra += 7000
    elif risk == "Medium":
        extra += 3000
    if smoker == "yes":
        extra += 5000

    final_premium = base + extra

    print("Base premium       : Rs.", base)
    print("Additional charges : Rs.", extra)
    print("Final premium      : Rs.", final_premium)
    if extra >= 10000:
        print("Risk message       : High Risk Policy")
    else:
        print("Risk message       : Standard policy")
