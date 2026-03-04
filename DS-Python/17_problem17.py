'''You have two lists:
ids = [101, 102, 103, 104]scores = [85, 92, 78, 95]
Create a dictionary student_scores with id as key and score as value, 
but only include students with score ≥ 90. Then, add 5 bonus points to
 those scores using a dictionary
 comprehension to create an updated version.
'''
ids = [101, 102, 103, 104]
scores = [85, 92, 78, 95]

student_score = {
   id : score
   for id, score in zip (ids, scores)
   if score >= 90
}

updated_score = {
    id : score + 5
    for id, score in student_score.items()
} 

print(updated_score)