#Findig the average of two numbers 
a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

print("The average of a and b :", (a+b)/ 2)
t = type((a+b)/2)
print(t)

# type conversion of the average value (My*)
print("The average of a and b :", (a+b)/ 2)
c = int((a+b/2))
t = type(c)
print(t)