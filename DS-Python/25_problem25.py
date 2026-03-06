''' Remove Missing Values + Average
Dataset
Create dictionary
student → average score
Rules
Ignore None
Round to 2 decimal places
Use dictionary comprehension'''

data = {
"Alice": [85, 90, None, 88],
"Bob": [None, 78, 82, 80],
"Charlie": [92, None, None, 95],
"David": [70, 75, 72, None]
}

new_dict = {
    name : round(sum(n for n in marks if n is not None) /
        len([n for n in marks if n is not None]),2
    )
    for name,marks in data.items()
}

print(new_dict)