class Computer:
    def __init__(self,cpu, ram, brand):
        self.cpu = cpu
        self.ram = ram
        self.brand = brand

    def config(self):
        print(f"CPU: {self.cpu}, RAM: {self.ram}, BRAND: {self.brand}")

com1 = Computer('i5','16GB','DELL')
com2 = Computer('AMD Ryzom 5','8GB','LENOVO')

com1.config()
com2.config()