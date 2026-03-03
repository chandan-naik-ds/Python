# Flatten the list and convert every word to uppercase.

nested_words = [["hi", "hello"], ["bye"], ["good", "morning"]]

new_words = [
    item.upper()
    for sublist in nested_words
        for item in sublist

]
print(new_words)