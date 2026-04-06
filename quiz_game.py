score = 0

answer1 = input("1. What is the capital city of Kenya? ").strip().lower()
if answer1 == "nairobi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer2 = input("2. How many days are there in a week? ").strip().lower()
if answer2 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer3 = input("3. Which planet is known as the Red Planet? ").strip().lower()
if answer3 == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer4 = input("4. What is 10 - 4? ").strip().lower()
if answer4 == "6":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer5 = input("5. Which programming language are you using for this project? ").strip().lower()
if answer5 == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz finished!")
print("Your score is", score, "out of 5")

if score == 5:
    print("Excellent work!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
