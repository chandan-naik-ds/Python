'''
Create dictionary
student → cleaned scores
Rule
Replace None with average of existing values
Example
"Alice": [85, 87.5, 90]'''


data = {
"Alice": [85, None, 90],
"Bob": [None, 78, 82],
"Charlie": [92, None, 95]
}

# clean = {}

# for name, scores in data.items():
#     valid = [x for x in scores if x is not None ]
#     avg = sum(valid)/ len(valid)

#     clean[name]= [avg if x is None else x for x in scores] 



# print(clean)

cleaned = {
    student : [
        (sum(x for x in scores if x is not None)/len([x for x in scores if x is not None]))
        if x is None else x 
        for x in scores
    ]
    for student , scores in data.items()
}

print(cleaned)