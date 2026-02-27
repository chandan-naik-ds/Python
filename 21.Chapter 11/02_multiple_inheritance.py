# Base class 
class Employee:
    def show(self,):
        company = "ITC"
        print(f"The name is {self.name},the salary is {self.salary}")
        print(f"The company is {self.company}")

class coder:
    def printlanguages(self):
        print(f"Out of all languages here is your language {self.language}")

# Inheritant class 
class Programmer(Employee,coder):
    company = "Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} he is good at {self.language} language")
        # print(f"The company is {self.company}")



# Create object of Programmer

p = Programmer()

# Assign attributes manually
p.name = "Chandan"
p.salary = 1200000
p.language = "Python"

# Call all the methods required
p.show()           # From Employee
p.printlanguages() # From coder 
p.showLanguage()   # From Programmer
