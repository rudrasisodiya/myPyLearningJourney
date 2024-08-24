class School:
    Name = 'Vellore Institute of technology'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

#Instance Method Defining (Using Instance variables)
    #1 Accessor Method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def set(self,m1):
        self.m1 = self.m1 +1
        return self.m1

#Class Method defination (using only Class variable)
    @classmethod
    def classMethod(cls):
        print(f"School Name is: {cls.Name}")

#Static Method defination (both Class and instance variables are not used)
    @staticmethod
    def staticMethod(val):
        return val/2

s1 = School(47,56,76)
s2 = School(67,96,36)

# Instance Methods calling
print(f"AVERAGE OF MARKS s1: {s1.avg()}") #Accessor Method
print(f"AVERAGE OF MARKS s2: {s2.avg()}") #Accessor Method

#Calling class method
School.classMethod()

#Calling static method
print(f"Static Method value divide by 2, Here is the result: {School.staticMethod(90)}")