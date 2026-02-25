# s = {1, 3, 56, 67, 32}

# s.add(566)
# print(s)

# s.update([5,4])
# print(s)

# s.remove(56)
# print(s)
# s.remove(566)
# print(s)
# s.remove(2)  # Gives error if the element is not found
# print(s)

# s.discard(4)
# print(s)
# s.discard(999) gives no error if not found
# print(s)

# v = s.pop()
# print(v)
# print(s)

# s.clear()
# print(s)

# s = {1, 3, 56, 67, 32}
# c = {1,2,3,4,5,6}

# print(s.union(c))

# print(s.intersection(c))

# print(s.difference(c)) # s-c

# print(s.symmetric_difference(c)) # prints the elements which are not common

a = {1, 2, 3, 4, 5, 6,}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(a.issubset(b)) # checks does all the elements of a exist in b & TRUE OR FALSE

print(a.issuperset(b))
print(b.issuperset(a))

print(a.isdisjoint(b)) # does both the sets have no single common elements