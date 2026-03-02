from functools import reduce
l = [5, 7, 8, 9, 10, 14, 15, 20, 220, 350, 500]

def maximum(a,b):
    if (a>b):
        return a
    return b

print(reduce(maximum, l))