class Employee:
    name = "chandan"
    language = "Python" 
    salary = 1200000 
    
    def __init__(self,name,salary,language): 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


chandan = Employee("Chanadn", 13000000, "Java")
chandan.name = "chandan"
print(chandan.name, chandan.language, chandan.salary)

