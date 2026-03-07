f = open("file.text")
print(f.reaad())
f.close()

# same thing can be written using with statement 

with open("file.txt") as f:
    print(f.reaad())

# You don't have to explicitly close the file the file will be automatically close when you exit with satatement