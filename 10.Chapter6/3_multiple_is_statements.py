a = int(input("Enter your age:"))

# if Statement 1
if(a%2==0):
    print("a is even") # Independent if in itsels
# end of if statement 1


# if statement 2
if(a>18):
    print("You  are above the age of consent")  # space is called indentation
    print("Good for you")
elif(a<0):
    print("You are entering invalid negative age")
elif(a==0):
    print("You are entering invalid zero age")
else:
    print("You are below the age of consent")

print("End of program")