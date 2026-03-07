'''
Create dictionary
student →
{
 'clean_scores':[...],
 'average':value,
 'max':value
}
Example output

{
'Alice':{'clean_scores':[85,90,88],'average':87.67,'max':90}
}'''

data = {
"Alice":[85,None,90,88],
"Bob":[None,78,82,80],
"Charlie":[92,None,None,95]
}
result = {
    student : {
        "clean_scores" : [s for s in scores if s is not None],
        "avg" : round(sum([s for s in scores if s is not None])/
                len([s for s in scores if s is not None]),2),
        "max" : max([s for s in scores if s is not None])
}

for student,scores in data.items()
}

print(result)