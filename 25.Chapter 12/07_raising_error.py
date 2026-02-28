a = int(input("Enter any number: "))
b = int(input("Enter any number: "))

if (b==0):
    raise ZeroDivisionError ("Our program is not meant to divide numbers by zero")
else:
    print(f"The divvision a/b is {a/b}")