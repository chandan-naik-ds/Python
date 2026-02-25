# remove 
def rem(l, word):
    l.remove(word)
    return l

l= ["Harry","Rohan","Mahesh","an"]

word = input("Enter any word: ")
print(rem(l, word))


# Strip
def rem(l, word):
    n = []
    for  item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
    

l= ["Harry","Rohan","Mahesh","an"]

word = input("Enter any word: ")
print(rem(l, word))