'''marks = [78, 45, 89, 67, 90, 34, 88, 76, 95, 54]
Your Tasks
Build a Python program that:
Calculate the average marks
Find the highest mark
Find the lowest mark
Create a new list of students who scored more than 75
Count how many students failed (assume fail mark < 40)
Expected Output Format (Example)
Average Marks: 71.6
Highest Marks: 95
Lowest Marks: 34
Students scoring above 75: [78, 89, 90, 88, 76, 95]
Number of failed students: 1'''

marks = [78, 45, 89, 67, 90, 34, 88, 76, 95, 54]

average_marks = sum(marks)/ len(marks)
print("Average marks: ",average_marks)

highest_marks = max(marks)
print("Highest marks: ",highest_marks)

lowest_marks = min(marks)
print("Lowest marks: ",lowest_marks)

high_scores = [m for m in marks if m>75] 
print("Students scoring above 75:",high_scores)

failed_students = [ m for m in marks if m<35]
print("Number of failed students: ", len(failed_students))