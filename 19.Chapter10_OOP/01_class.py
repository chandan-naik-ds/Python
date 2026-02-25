class Employee:
    language = "Py" # Class attribute
    salary = 1200000 # Class attribute

chandan = Employee()
chandan.name = "Chandan" # Instance(object) attribute
print(chandan.name,chandan.language,chandan.salary)

viraj = Employee()
viraj.name = "Viraj" # Instance(object) attribute
print(viraj.name,viraj.language,viraj.salary)

''' Here name is Instance(object) attribute and language,salary are the class attributes as they directly
  belong to class '''
