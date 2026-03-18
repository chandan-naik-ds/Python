# Find whether the person is a senior citizen or not

from datetime import date

PerName = input("Enter the name of the person: ")
PerBirthyear = int(input("Enter the Birth year of the person: "))

CurYear = date.today().year
print("Current year:",CurYear)

PerAge = CurYear - PerBirthyear
print("Persons Age:",PerAge)

if (PerAge > 60):
        print(PerName,"aged",PerAge ,"years is a senior citizen")
  
else:
        print(PerName,"aged",PerAge ,"years is not a senior citizen")