'''words = ["data","science","data","python","ai","python","data","ml","ai","ai"]
Create dictionary:
word → frequency
But only include words appearing more than twice.
Expected format
{'data':3,'ai':3}
Constraint:
Must use dictionary comprehension
Must use count() or manual frequency logic'''


words = ["data","science","data","python","ai","python","data","ml","ai","ai"]

new_word = {
    word: words.count(word)
    for word in set(words)
    if words.count(word)>2
}
print(new_word)

