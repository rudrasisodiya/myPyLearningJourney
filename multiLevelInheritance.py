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

class C(B):
    def func5(self):
        print("Function5")
    def func6(self):
        print("Function6")

a = C()
a.func1()
a.func5()
a.func3()