'''b. Develop a program to read the name and year of birth of a
person. Display whether the person is asenior citizen or not.'''

name = input("Enter the name of the person: ")
birth_year = int(input("Enter the birth year of a person: "))

age = 2026 - birth_year

if age>60:
    print(name,"is a senior citizen")
else: 
    print(name,"is not a senior citizen")