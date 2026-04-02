marks = float(input("Enter Students  marks:"))

if(marks<=100 and marks >=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "c"
elif(marks<50):
    grade = "Fa"

print("The Student Grade is :",grade)