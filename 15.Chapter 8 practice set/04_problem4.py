# recursive function to find the sum of first n natural numbers 

'''
sum(1) = 1
sum(1) = 1 + 2
sum(1) = 1 + 2 + 3
sum(1) = 1 + 2 + 3 + 4
sum(1) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 +......n
sum(n) = sum(n-1)+n
'''

# def sum(n):
#     if(n==1):
#          return 1
#     return sum(n-1)+n

# n = int(input("Enter any number: "))
# print(sum(n))


def sum(n):
    total = 0
    for i in range (1, n+1):
        total += i
    return total
    
n = int(input("Enter any natural number: "))
result = sum(n)
print(f"Sum = {result}")



