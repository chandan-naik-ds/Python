n = int(input("Enter any number: "))

l = [n*i for i in range(1, 11)]



with open("Tables.txt", "a") as f:
    f.write(f"Tables of {n} : {str(l)} \n")