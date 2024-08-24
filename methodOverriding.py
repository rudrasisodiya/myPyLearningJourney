class Base:
    def show(self):
        print("Inside Base Class")
class Sub(Base):
    #pass
    def show(self):
        print("Inside Derived Class")

i = Sub()
i.show()

#When we call function/method present in both base and derived (sub) class, then it will be called first sub (derived) class
