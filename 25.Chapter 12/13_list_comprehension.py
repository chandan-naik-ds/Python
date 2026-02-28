Mylist = [1, 3, 5, 7, 9, 12]

# Squaredlist = []
# for i in Mylist:
#     Squaredlist.append(i*i)

# the same can be simplified by list comprehension

Squaredlist = [i*i for i in Mylist]


print(Mylist)
print(Squaredlist)