'''Flatten Nested List Data
Dataset
Create dictionary
student → flattened score list
Expected
{
'Alice':[85,90,88],
'Bob':[78,82,80],
'Charlie':[92,95]
}'''

data = {
"Alice": [[85, 90], [88]],
"Bob": [[78], [82, 80]],
"Charlie": [[92, 95]]
}

new_dict = {
    name : [item for sublist in nested for item in sublist ]
    for name,nested in data.items()
}

print(new_dict)