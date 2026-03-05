'''
Create dictionary:
student → average score
Rules
Ignore None
Use dictionary comprehension
Example output
{
'Alice':87.67,
'Bob':80,
'Charlie':93.5,
'David':72.33
}'''


data = {
"Alice": [85, 90, None, 88],
"Bob": [None, 78, 82, 80],
"Charlie": [92, None, None, 95],
"David": [70, 75, 72, None]
}

new_dict = {
    name : sum(n for n in marks if n is not None)/
        len([n for n in data if n is not None ])
    for name,marks in data.items()
}

print(new_dict)