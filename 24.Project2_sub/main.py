import random

e = random.randint(1, 50)   # easy
m = random.randint(1, 100)  # medium 
h = random.randint(1, 500)  # hard

l = input("Select the level (easy/medium/hard): ").lower()

if l == "easy":
    print("--- Easy level ---")
    number = e
    max_attempts = 7

elif l == "medium":
    print("--- Medium level ---")
    number = m
    max_attempts = 14

elif l == "hard":
    print("--- Hard level ---")
    number = h
    max_attempts = 25

else:
    print("Invalid level selected!")
    exit()

guesses = 0

while guesses < max_attempts:
    a = int(input("Guess the number: "))
    guesses += 1

    if a == number:
        print(f"You guessed the number {number} correctly in {guesses} attempts!")
        break
    elif a > number:
        print("Lower number please")
    else:
        print("Higher number please")

if guesses == max_attempts and a != number:
    print(f"Game Over! The correct number was {number}")