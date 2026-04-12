num = int(input("Enter the Fibonacci sequence length to be genertaed : "))

firstTerm = 0
secondTerm = 1

print("The Fibonacci series with",num, "term is :")
print(firstTerm, secondTerm, end="")
for i in range (2,num):
    curTerm = firstTerm + secondTerm
    print(curTerm, end="")
    firstTerm = secondTerm
    secondTerm = curTerm