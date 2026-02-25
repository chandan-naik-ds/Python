# string is data type in python
# string is a sequence of characters enclosed in quotes 
# String is immutable

#wecan primarily write string in 3 ways 

a = "Chandu"
b = 'Chandu'
c = '''Chandu'''

# slicing; string can be sliced to get parts
name = "Chandan"

nameshort = name[0:3] # start from index 0 all the way till 3(excluding 3)
print(nameshort)
character = name[2]
print(character)

name[0] = "v"
print(name)  # Gives error because strings are immutable