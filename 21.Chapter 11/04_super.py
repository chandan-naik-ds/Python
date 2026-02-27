class Employee:
    a = 1
    def __init__(self):
        print("Constructor of Employee")

class Programmer(Employee):
    b = 2
    def __init__(self):
        print("Constructor of Programmer")
        

class manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    

# o = Employee()
# print(o.a)  

# p = Programmer()
# print(p.a,p.b)

q = manager()
print(q.a,q.b,q.c)