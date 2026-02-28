# try:
#     a = int(input("Enter any number: "))
#     print(a)

# except Exception as e:
#     print("Hello")
#     print(e)

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter dinominator: "))

    result = a/b
    print(f"Result : {result}")

except ZeroDivisionError:
    print("You cannot divide by zero")

except Exception as e:
    print("Some other error occured pleaase check is out!")
    print(e)


try:
    a = input("Enter numerator: ")
    b = 5

    result = a + b # This will cuase Typeerror
    print(f"Result : {result}")

except TypeError:
    print("Type error occured! You cannot add string and integer")



# try:
#     a = input("Enter numerator: ")
#     b = 5

#     result = a + b # This will cuase Typeerror
#     print(f"Result : {result}")

# except:
#     print("Something wrong")


try:
    a = int(input("Enter numerator: "))
    b = 5

    result = a + b # This will cuase Typeerror
    print(f"Result : {result}")

except TypeError:
    print("Type error occured! You cannot add string and integer")

except:
    print("Something wrong")
