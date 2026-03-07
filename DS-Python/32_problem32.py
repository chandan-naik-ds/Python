'''Remove Outliers

Dataset

data = {
"Alice":[85, 90, 300],
"Bob":[78, 82, 80],
"Charlie":[92, 95, 500]
}

Create dictionary

student → scores < 100'''


data = {
"Alice":[85, 90, 300],
"Bob":[78, 82, 80],
"Charlie":[92, 95, 500]
}

dictonary = {}

for student,scores in data.items():
    dictonary[student] = [score for score in scores if score<100]
    

print(dictonary)