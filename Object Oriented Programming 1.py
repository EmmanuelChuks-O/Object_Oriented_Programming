# object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book
#         You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, color, model, year, for_sale, price):
        self.color = color
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price = price

    def drive(self):
        print(f"Emmanuel are driving the {self.color} {self.model}")

    def stop(self):
        print(f"Emmanuel should stop driving the {self.color} {self.model}")

    def describe(self):
        print(f"The {self.color} {self.year} {self.model} is for sale at a price of ${self.price}.")


car1 = Car(color="Black", model="Honda CR-V", year=2020, for_sale=True, price=5000)
car2 = Car("White", "Mazda CRX", 2021, True, 21000)
print(car2.color)
print(car2.model)
print(car2.year)
print(car2.for_sale)
print(f"${car2.price}")

car2.drive()
car1.stop()

car1.describe()
car2.describe()