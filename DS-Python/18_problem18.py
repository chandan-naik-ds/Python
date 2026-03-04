'''Given freq = {"a": 5, "b": 2, "c": 8, "d": 1} (letter frequencies),
create a new dict with only items where frequency > 3, sorted by value descending. 
Output format: {letter: count}.'''

freq = {"a": 5, "b": 2, "c": 8, "d": 1}

# dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
freq = {"a": 5, "b": 2, "c": 8, "d": 1}

new_dict = dict(
    
    sorted(
    {letter:count for letter,count in freq.items() if count>3}.items(),
    # key = lambda  x : x[1],
    reverse = True
    )
)

print(new_dict)







'''

new_dict = dict(
    sorted(
        {letter: count for letter, count in freq.items() if count > 3}.items(),
        key=lambda x: x[1],
        reverse=True
    )
)'''