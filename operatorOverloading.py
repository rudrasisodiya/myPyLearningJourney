class Random:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def __add__(self, other):
        var1 = self.var1 + other.var1
        var2 = self.var2 + other.var2
        run3 = Random(var1,var2)
        return run3

    def __gt__(self, other):
        r1 = self.var1 + self.var2
        r2 = other.var1 + other.var2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.var1,self.var2)


run1 = Random(57,98)
run2 = Random(78,48)

run3 = run1 + run2

print(run3.var1)

if run1 > run2:
    print("run1 Greater")
else:
    print("run2 Greater")


#When One wants to perform operation on user defined objects then need to use functions like above to perform desired actions

print(run1.__str__())
print(run1)

#Whenever we perform basic arithmetic operations using operators, behind the seen it all done using magic methods as above defined
