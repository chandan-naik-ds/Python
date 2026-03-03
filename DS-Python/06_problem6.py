# Create a list of "PASS" for marks ≥ 40 and "FAIL" otherwise using a single comprehension.

marks = [45, 78, 90, 33, 67, 88, 25]

PASS = [i for i in marks if i >=40]

print(PASS)

FAIL = [i for i in marks if i <=40]

print(FAIL)


