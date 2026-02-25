#  Finding the factorial of any number using recursion

def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter any number: "))
print(f"factorial of any number is: {factorial(n)}")