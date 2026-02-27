# class Number:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n
# n = Number(1)
# m = Number(2)
# print(n+m)

class Number:
    def __init__(self,n):
        self.n = n

    def __mul__(self, num):
        return self.n * num.n


n = Number(1)
m = Number(2)

print(n*m)

# __sub__
# __trudiv__
# __floordiv__
# __len__