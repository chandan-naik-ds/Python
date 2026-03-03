
'''
Create a list of numbers that are:

divisible by 2

NOT divisible by 4'''

numbers = range(1, 31)

l1 = [i for i in numbers if i%2==0]
l2 = [i for i in numbers if i%4!=0]
print(l1)
print(l2)