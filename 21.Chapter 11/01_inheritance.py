class Employee:
    def show(self,):
        company = "ITC"
        print(f"The name is {self.name},the salary is {self.salary}")

    def __init__(self,name,salary,language):
        self.name = "Chandan"
        self.salary = 120000
        self.language = "Python"


class Programmer(Employee):
    company = "Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} he is good at {self.language} language")


# Create object of Programmer
p = Programmer("Chandan",1200000,"Python")
# p = Programmer()

# # Assign attributes manually
# p.name = "Chandan"
# p.salary = 1200000
# p.language = "Python"

# Call both methods
p.show()           # From Employee
p.showLanguage()   # From Programmer