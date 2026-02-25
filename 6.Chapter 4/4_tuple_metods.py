# Since the tuples are immutable they have very few methods compared to lists

T = (23,45,"Ravi",345,23,46,98)

# count
t1 = T.count(23)
print(t1)

#  Index
t2 = T.index("Ravi")
print(t2)

# Max 
num = (23,45,54,56,678,)
num1 = max(num)
print(num1)

# MIN
num2 = min(num)
print(num2)

# Sum
num3 =sum(num)
print(num3)

#length
num4 = len(num)
print(num4)

# Sequenece
t = ([1,2,3])
tuple1 = tuple(t)
print(tuple1)

# in / not in 
T1 = (10, 20, 30)
T2 = (40, 50, 60)

print(20 in T1)
print(70 in T2)

# Add 2 tuples     +
t3 = (T1 + T2)
print(t3)


#   *  Repetition
t4 = T1*3
print(t4)

# Index
t5 = T1.index(20)
print(t5)