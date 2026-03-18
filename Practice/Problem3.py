# '''a. Develop a program to generate Fibonacci sequence of length (N).
# Read N from the console'''


# n = int(input("Enter any number: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end= " ")
#     a,b = b, a+b



list = [1, 3, 4, 5, 6, 7]
print(list)
list.insert(1, 2)
list.append(9)
print(list)
list.remove(9)
print(list)
print(len(list))
list.pop(2)
print(list)

list.clear()
print(list)