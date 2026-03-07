'''Nested Dictionary Cleaning

Dataset

students = {
"Alice":{"math":85,"science":90,"english":None},
"Bob":{"math":78,"science":None,"english":80},
"Charlie":{"math":92,"science":95,"english":88}
}

Create dictionary
student → average score
Rules
Ignore None'''


data = {
"Alice":{"math":85,"science":90,"english":None},
"Bob":{"math":78,"science":None,"english":80},
"Charlie":{"math":92,"science":95,"english":88}
}

clean = {}

for student, subjects in data.items():
    clean[student] = {sub: score for sub, score in subjects.items() if score != None}

print(clean)