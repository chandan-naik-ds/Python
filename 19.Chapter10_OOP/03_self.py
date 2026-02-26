class Employee:
    language = "Python" 
    salary = 1200000 

    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}")
    
    @staticmethod   # decorator to mar greet as static method 
    def greet(self):
        print("Congratulations")

chandan = Employee()
# chandan.language = "Java script" 
chandan.getInfo()
# Employee.getInfo(chandan)
# chandan.greet()
Employee.greet(chandan)