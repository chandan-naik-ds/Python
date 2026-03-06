'''data = {
"Alice":[50,60,70],
"Bob":[30,40,50],
"Charlie":[80,90,100]
}
Create dictionary
student → scaled scores
Rule
new_value = value / 100
Expected
"Alice":[0.5,0.6,0.7]'''

data = {
"Alice":[50,60,70],
"Bob":[30,40,50],
"Charlie":[80,90,100]
}

dictonary = {}

for name,values in data.items():
        dictonary[name] = []

        for value in values:
            new_value = value /100
            dictonary[name].append(new_value)


print(dictonary)