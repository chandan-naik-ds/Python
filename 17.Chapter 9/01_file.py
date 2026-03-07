# txt files can be read in following way by code 

f = open("file.txt", "r") # open is built in function in c 

data = f.read()
print(data)
f.close()