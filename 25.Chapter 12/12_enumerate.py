l = [23, 45, 56, 78]

# index = 0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index += 1

# the same can be simplified using enumerate

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")