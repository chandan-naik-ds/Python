def MyFunc():
    print("Hello Python")

# MyFunc()
# print(__name__)

if __name__ == "__main__":
    # if this code is directly executed by its own file
    print("We are directly running this code")
    MyFunc()
    print(__name__)