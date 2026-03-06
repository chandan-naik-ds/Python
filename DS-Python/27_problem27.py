'''Student Pass/Fail Classification
Dataset
Create dictionary
student → "Pass" or "Fail"
Rule
average >= 50 → Pass
average < 50 → Fail'''


data = {
"Alice": [85, 90, 88],
"Bob": [40, 35, 45],
"Charlie": [60, 62, 58],
"David": [25, 30, 28]
}

new_dict = {
    name : "Pass" if sum(marks)/len(marks)>= 50 else "Fail"
    for name,marks in data.items()
}

print(new_dict)