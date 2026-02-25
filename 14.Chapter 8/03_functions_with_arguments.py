def goodDay(name):  # name - variable
    print("Good day " + name)

goodDay("Chandan")  #Chandan - Argument
goodDay("Mahesh")  
goodDay("Ravi") 


def goodDay(name, ending):  # name - variable
    print("Good day " + name)
    print(ending)

goodDay("Chandan", "Thankyou")  #Chandan - Argument
goodDay("Mahesh", "Thankyou")  
goodDay("Ravi", "Thankyou")


# returning values to variable 
def goodDay(name, ending):  # name - variable
    print("Good day " + name)
    print(ending)
    return "Ok"

a = goodDay("Chandan", "Thankyou")
print(a)