class Car:
    Wheels = 4

    def __init__(self):
        self.mil = 15
        self.brand = "TATA"

c1 = Car()
c2 = Car()

#Modifying variable in class namespace
Car.Wheels = 5

print(f"TATA CAR PROPERTIES: 'MILAGE = {c1.mil}', 'BRAND = {c1.brand}', 'WHEELS = {c1.Wheels}'")
print(f"TATA CAR PROPERTIES: 'MILAGE = {c2.mil}', 'BRAND = {c2.brand}', 'WHEELS = {c2.Wheels}'")