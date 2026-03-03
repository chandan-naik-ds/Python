'''Flatten this nested list using a single list comprehension:
nested = [[1,2,3], [4,5], [6,7,8,9], [10]]
→ Output: [1,2,3,4,5,6,7,8,9,10]'''

nested = [[1,2,3], [4,5], [6,7,8,9], [10]]

flatten_list = [ item for sublist in nested for item in sublist]

print(list(flatten_list))