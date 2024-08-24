class Random:
    def sum(self,a=None,b=None,c=None):
        s =0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s

run = Random()

print(f"Method Overloading: {run.sum(98,68,93)}")
print(f"Method Overloading: {run.sum(68,93)}")
print(f"Method Overloading: {run.sum(93)}")