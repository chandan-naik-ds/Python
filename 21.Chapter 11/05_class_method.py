class students:
    s = 1

    @classmethod
    def show(cls):
        print(f"The class atribute a is {cls.s}")

e = students()
e.s = 45

e.show()