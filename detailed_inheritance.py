# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent C(B) <-B(A) <- A

# multiple inheritance 

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Grass")
hawk = Hawk("Fish")
fish = Fish("Worms")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
hawk.eat()
fish.eat()
rabbit.sleep()
hawk.sleep()
fish.sleep()


