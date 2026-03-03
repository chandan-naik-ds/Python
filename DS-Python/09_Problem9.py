names = ["arun", "Isha", "om", "Eshan", "rahul", "Uma"]
'''
Create a list of names that:

start with vowel

length is greater than 3

convert to uppercase'''

new_names= [name.upper() for name in names
            if len(name)>3 and name[0].lower() in "aeiou"]

print(new_names)