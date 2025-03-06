# object = a bundle of related attributes (variables) and mthods (functions)
#        => Ex. phone, cup, book
#        => You need a class to create many objects


# class = a blueprint used to design the structure of an object


from classes.car import Car

car1 = Car("Toyota", 2020, "Red", True)
car2 = Car("BMW", 2024, "Green", False)
car3 = Car("Audi", 2022, "Blue", True)

print(car1.color, "\n", car1.year,"\n", car1.model,"\n", car1.for_sale)
print(car2.color, "\n", car2.year,"\n", car2.model,"\n", car2.for_sale)
print(car3.color, "\n", car3.year,"\n", car3.model,"\n", car3.for_sale)

# Methods => are actions tht our objects can perfom
