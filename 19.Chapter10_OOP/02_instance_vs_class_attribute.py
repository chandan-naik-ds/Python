class Employee:
    language = "Python" # Class attribute
    salary = 1200000 # Class attribute

chandan = Employee()
chandan.language = "Java script" # Instance(object) attribute
print(chandan.language,chandan.salary)

'''Here the Java script will be printed as a language because Instance attributes
 take the preference over a class attributes during assignment and retrivel'''


