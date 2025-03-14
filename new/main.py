# class

class Dog:

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("Woof!")


d = Dog()
d.bark()
print(d.add_one(5))
print(type(d))
