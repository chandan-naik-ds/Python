# Flatten and divide each number by 10.

matrix = [[10, 20], [30, 40], [50, 60]]


new_matrix = [
    item/10
    for sublist in matrix
    for item in sublist
    
]

print(list(new_matrix))