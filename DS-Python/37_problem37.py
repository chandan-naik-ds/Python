'''Given text = "Data Science is awesome! Python is powerful for data analysis.",
create a list of words (split by space) that are longer than 4 characters,
reversed, and in uppercase — using one comprehension.'''

text = "Data Science is awesome! Python is powerful for data analysis."

new_list = [ word[::-1].upper() for word in text.split() if len(word) > 4]

print(new_list)