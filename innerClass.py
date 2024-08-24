class Student:

    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        #Inner class object creation inside main class or main class's constructor
        self.l1 = self.Laptop('AMD RYZON 5 series','16 GB','LENOVO IDEAPAD SLIM 1')

    def show(self):
        print(f"Student Details:\nNAME: {self.name}\nAGE: {self.age}\nHEIGHT: {self.height}")
        #Calling inner class method inside main class method
        self.l1.show()

    class Laptop:

        def __init__(self,cpu,ram,brand):
            self.cpu = cpu
            self.ram = ram
            self.brand = brand

        def show(self):
            print(f"Laptop Details:\nCPU: {self.cpu}\nRAM: {self.ram}\nBRAND: {self.brand}")

s1 = Student('Rudra',28,'168cm')
s1.show()

#Inner Class callling ouside Using main class name and creating object
#l1 = Student.Laptop('AMD RYZON 5 series','16 GB','LENOVO IDEAPAD SLIM 1')
#l1.show()