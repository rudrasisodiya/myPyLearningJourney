class Original:
    def show(self):
        print("Original Duck")
        print("Walk")
        print("Run")
        print("Go")

class Duplicate:
    def show(self):
        print("Duplicate Duck")
        print("Walk")
        print("Run")
        print("Go")

class Marathon:
    def go(self,o):
        o.show()

o = Duplicate()
#o = Original()
m = Marathon()
m.go(o)
o.show()