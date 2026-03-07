'''data = {
"Alice":{"math":[80,85],"science":[90,88]},
"Bob":{"math":[70,75],"science":[60,65]}
}
Create dictionary
student → overall average score
Example
"Alice":85.75'''

data = {
"Alice":{"math":[80,85],"science":[90,88]},
"Bob":{"math":[70,75],"science":[60,65]}
}

clean = {
    student: sum(score for subject in subjects.values() for score in subject)/
    sum(len(subject) for subject in subjects.values())
    for student,subjects in data.items()
}

print(clean)