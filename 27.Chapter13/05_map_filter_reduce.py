from functools import reduce
# Map Example
# l = [1, 2, 3, 4, 5, 6, 7,]

# square = lambda x: x*x

# sqllist = map(square, l)

# print(list(sqllist))

# filter example

l = [1, 2, 3, 4, 5, 6, 7,]

def even(n):
    if(n%2 == 0):
        return True
    return False

evenlist = filter(even, l)
print(list(evenlist))

def sum(a,b):
    return a + b
    return a * b

mul = lambda a,b:a*b
print(reduce(sum, l))
print(reduce(mul, l))