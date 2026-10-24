# Mini Project 2: Password Strength Checker
import string


def check_password(password):
    """Return (score, list of problems) for the password."""
    problems = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        problems.append("Use at least 8 characters")

    has_upper = has_lower = has_digit = has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_special = True

    if has_upper:
        score += 1
    else:
        problems.append("Add an uppercase letter")
    if has_lower:
        score += 1
    else:
        problems.append("Add a lowercase letter")
    if has_digit:
        score += 1
    else:
        problems.append("Add a digit")
    if has_special:
        score += 1
    else:
        problems.append("Add a special character (e.g. @, #, $)")

    return score, problems


def main():
    password = input("Enter a password to check: ")

    if password == "":
        print("Password cannot be empty")
        return
    if " " in password:
        print("Password must not contain spaces")
        return

    score, problems = check_password(password)


    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword strength:", strength, "(score " + str(score) + "/5)")
    if problems:
        print("How to improve:")
        for p in problems:
            print(" -", p)


main()
