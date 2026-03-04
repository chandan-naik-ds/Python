# Create a list containing only words with length > 3, converted to Title Case.

words = ["python", "AI", "data", "ML", "engineering", "code"]

new_words = [i.upper() for i in words if len(i)>3 ]

print(new_words)