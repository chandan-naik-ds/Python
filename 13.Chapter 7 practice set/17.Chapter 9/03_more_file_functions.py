f = open("file.txt")

# lines = f.readlines()
# print(lines)
# print(type(lines))

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)

# line5 = f.readline()  # empty string becoz no 5th line
# print(line5 == "") # "" - empty string

# f.close()
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()