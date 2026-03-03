# Flatten it but include only even numbers


nested = [[1,2], [3,4,5], [6], [7,8,9]]

new_shift = [
    item for sublist in nested for item in sublist 
    if item %2 ==0]

print(list(new_shift))
