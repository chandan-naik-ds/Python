'''Remove Invalid Values
Dataset
Create dictionary
student → valid scores list
Rules
Remove values <0 or >100
Expected example
{
'Alice':[85,90,88],
'Bob':[78,82,80],
'Charlie':[92,95],
'David':[70,75,72]
}'''

scores = {
"Alice": [85, -1, 90, 88],
"Bob": [78, 82, 500, 80],
"Charlie": [92, 95, -5],
"David": [70, 75, 72]
}

new_dict = {
    name : [n for n in score if n>0 and n<100 ]
    for name, score in scores.items()
}

print(new_dict)