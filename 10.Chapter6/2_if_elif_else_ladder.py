a = int(input("Enter your age:"))

# If elif else ladder
if(a>18):
    print("You  are above the age of consent")  # space is called indentation
    print("Good for you")
elif(a<0):
    print("You are entering invalid negative age")
elif(a==0):
    print("You are entering invalid zero age")
else:
    print("You are below the age of consent")

print("End of program") # If if codition istrue the controlignore else and also printsthis statement
