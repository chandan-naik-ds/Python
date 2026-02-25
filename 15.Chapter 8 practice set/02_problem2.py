# Converting celcius to fahrenheit using functions
# F c*(9/5)+32
def fahrenheit(deg):
    return deg*(9/5)+32
    

deg  = int(input("Enter the temp in degrees: "))
print(fahrenheit(deg))

# Converting fahrenheit to celcius using functions
# C = (f-32)*(5/9)

# def celcius(F):
#     return (F-32)*(5/9)

# F = int(input("Enter temperature in Fahrenheit: "))
# print(celcius(F))


def celcius(F):
    return (F-32)*(5/9)

F = int(input("Enter temperature in Fahrenheit: "))
print(f"{celcius(F)} °c")