# Mini Project 8: Quiz Application
# questions and answers are stored together in a list of tuples
questions = [
    ("What is the capital of India?", "delhi"),
    ("Which language is this quiz written in?", "python"),
    ("How many days are there in a week?", "7"),
    ("What is 12 x 12?", "144"),
    ("Which planet is known as the Red Planet?", "mars"),
]

score = 0
total = len(questions)

print("===== PYTHON QUIZ =====")
for number, (question, answer) in enumerate(questions, start=1):
    user_answer = input("Q" + str(number) + ". " + question + " ").strip().lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer is", answer)

percentage = score / total * 100

print("\n------ RESULT ------")
print("Score      :", score, "/", total)
print("Percentage :", percentage, "%")
if percentage >= 80:
    print("Performance: Excellent")
elif percentage >= 60:
    print("Performance: Good")
else:
    print("Performance: Keep Practicing")
