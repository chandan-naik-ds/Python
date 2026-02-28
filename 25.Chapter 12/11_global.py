a = 89

def fun():
    a = 3
    print(a)

fun()
print(a)

# output : 3 & 89
# above global variable a = 89 
# we can change the global variable value using global key word 

a = 89

def fun():
    global a
    a = 3
    print(a)

fun()
print(a)

# output : 3 & 3