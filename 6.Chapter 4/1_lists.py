# Python lists are the containers to store the values of any data type

all = ["Apple","Rohan", 23, 345.77, "Ramesh"]

print(all)
print(all[1])
all[1] = "Mahesh"
print(all[1])
print(all)  
# Here the original lisitem can be replaced hence the list are 
# mutable in python
# lists can be indexed as a string 

# slicing can be done in lists same as strings 

print(all[1:5])
print(all[0:])
print(all[1:3])
print(all[:5])
print(all[1:1]) # Empty

all[1] = "Grapes"
print(all)