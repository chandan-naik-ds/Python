'''a. Develop a program to generate Fibonacci sequence of length (N).
Read N from the console'''


n = int(input("Enter any number: "))

a = 0
b = 1

for i in range(n):
    print(a, end= " ")
    a,b = b, a+b