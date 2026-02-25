with open("log.txt") as f:
    content = f.read()

    if("python" in content):
        print("Python found!")
    else:
        print("Python not found!")