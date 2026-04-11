# 1. Get user input and convert it to an integer
number = int(input("Enter a number: ")) 

# 2. Check the remainder when divided by 2
# Any even number divided by 2 gives a remainder of 0
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    # If the remainder is 1, the number is odd
    print(f"{number} is an Odd number.")
