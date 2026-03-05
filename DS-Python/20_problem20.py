'''Create a dictionary containing only students scoring ≥ 80, but the value should be:
(score, grade)'''

students = {
"Alice": 88,
"Bob": 95,
"Charlie": 67,
"David": 92,
"Eve": 78,
"Frank": 85
}

dictonary = {
    name : (score, "A" if score>= 90 else "B")
    for name, score in students.items()
    if score >= 80
}

print(dictonary)