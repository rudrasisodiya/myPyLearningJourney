class A:
    def __init__(self):
        print("Init of A")

    def fun1(self):
        print("Function1 - A")

    def fun2(self):
        print("Function2")

class B():
    def __init__(self):
        print("Init of B")

    def fun1(self):
        print("Function1 - B")

    def fun4(self):
        print("Function4")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Init of C")

    def feature(self):
        super().fun4()

c = C()
c.fun1()
#MRO (Method resolution Order), It always start executing method, constructor execution from left to right side
c.feature()
# To represent Super class, we use super method