class A:

    def __init__(self):
        print("Init of A")

    def fun1(self):
        print("Function1")

    def fun2(self):
        print("Function2")

class B(A):

    def __init__(self):
        #Calling Base class A's constructor in Derived Class B
        super().__init__()
        print("Init of B")

    def fun3(self):
        print("Function3")

    def fun4(self):
        print("Function4")

#When we call object of any class, constructor of that perticular class only invoked/called that time, let's say you want to call Base class A's constructor in Derived class B then use super().constructore_name() of Base Class A

a = B()