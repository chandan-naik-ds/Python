class sample:
    a = 5

object = sample()
print(object.a) # Prints class attribute becoz instance attribute is not present
object.a = 0 # Now the instance attribute is set
print(object.a) # Prints instance attribute becoz instance attribute is  present

print(sample.a) # This prints again the class attribute showing that the prsence of instance attribute
                #does not change the class attribute 
