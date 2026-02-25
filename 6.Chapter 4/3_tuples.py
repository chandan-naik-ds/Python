# tuple is immutable data type in python
# Tuple are immutabele

a = (1,2,3,4,5)
print(type(a))

# Empty tuple
b =()
print(b)

#if you give 
c = (1) # python will understand it lke a int so you may  add comma to 
# show it as a tuplee
print(type(c))  #class int

d = (1,)
print(type(d)) #class tuple


e = (1,"Rohan","Mahesh",345.99,"Grapes")
e[0] = 2 # Gives error
print(e)