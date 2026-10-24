# Mini Project 5: Number Guessing Game
secret = 37
max_attempts = 5
attempts = 0
won = False

print("I have chosen a number between 1 and 100. You have", max_attempts, "guesses.")

while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print()
if won:
    print("Congratulations! You guessed it.")
else:
    print("You lost. The secret number was", secret)
print("Attempts used:", attempts)
