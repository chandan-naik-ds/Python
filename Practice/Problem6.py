def Swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20
result = Swap(x, y)
print(result)
