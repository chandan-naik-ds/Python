
try:
    a = int(input("Enter numerator: "))
    print(a)

except Exception as e:
    print("Some other error occured pleaase check is out!")
    print(e)

else:
    print("Hey you enterd inside the else")  # Executes only if try was successfull