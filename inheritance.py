# inheritance = Allows a class to inherit aattributes and methods from another class
# Parent class = The class being inherited from
# Child class = The class that inherits from another class
# Helps with code reusability and extensibility

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")

print(dog.name)
print(cat.name)
print(mouse.name)

print(dog.is_alive)
print(cat.is_alive)
print(mouse.is_alive)

dog.eat()
cat.eat()
mouse.eat()
    
dog.sleep()
cat.sleep()
mouse.speak()

dog.speak()
cat.speak()
mouse.speak()