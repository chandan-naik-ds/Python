with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if (content1==content2):
    print("Yes both the files are identical")
else:
    print("No both the files are identical")
