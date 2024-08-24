class A:
    def func1(self):
        print("Function1")
    def func2(self):
        print("Function2")

class B(A):
    def func3(self):
        print("Function3")
    def func4(self):
        print("Function4")

a = B()
a.func1()
a.func4()