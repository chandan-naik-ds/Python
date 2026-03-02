l = [5, 7, 8, 9, 10, 14, 15, 20, 220, 350, 500]

def devisible(n):
    if(n%5 == 0):
        return True
    return False

divisibleL = filter(devisible,l)
print(list(divisibleL))