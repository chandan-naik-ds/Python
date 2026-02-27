class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a)  # Prints a attribute
# print(o.b)  # Shows an error as there is no b attribute in Employee class

p = Programmer()
print(p.a,p.b)

q = manager()
print(q.a,q.b,q.c)

