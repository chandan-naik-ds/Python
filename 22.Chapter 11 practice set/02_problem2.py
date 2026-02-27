class Animals:
    def __init__(self,name):
        self.name = name

    def eats(self):
        print(f"{self.name} is eating")
        

class Pets(Animals):
    def __init__(self, name , owner):
        super().__init__(name)
        self.owner = owner

    def show_owner(self):
        print(f"{self.name}'s owner is {self.owner}")

      

class Dog(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Bow!!")
        print(f"Tommy is of {self.breed} Breed")

# a = Animals("Tommy")
# print(a.name)
# a.eats()
# b = Pets("Tommy","Chandan")
# print(b.owner)
# b.show_owner()
# c = Dog("Tommy","Chandan","Lab")
# c.bark()


# or


d = Dog("Tommy","Chandan","Labrador")
# print(d.name)
# print(d.owner)
# print(d.breed)
d.eats()
d.show_owner()
d.bark()


