class Employee:
    def __init__(self,salary, Increment):
        self.salary = salary
        self.Increment = Increment # 0.10 for 10%

    @property
    def SalaryAfterIncrement(self):
        return self.salary + (self.salary * self.Increment)
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, new_salary):
        self.Increment = (new_salary - self.salary)/self.salary

e = Employee(50000, 0.10)
print("Current Salary after Increment",e.SalaryAfterIncrement)

e.SalaryAfterIncrement = 60000
print("New Increment",e.Increment)
print("Updated salary after new increment",e.SalaryAfterIncrement)


