class Sorting:
    def __init__(self,lst):
        self.lst = lst

    def get_input(self):
        size = int(input("Enter How many numbers you would like to enter: "))
        for i in range(size):
            val = int(input(f"Insert {i+1} number: "))
            self.lst.insert(i,val)

    def sort(self):
        for i in range(len(self.lst)-1,0,-1):
            for j in range(i):
                if self.lst[j]>self.lst[j+1]:
                    temp = self.lst[j]
                    self.lst[j] = self.lst[j+1]
                    self.lst[j+1] = temp

        print("SORTED LIST: ",self.lst)

lst = []
obj = Sorting(lst)
obj.get_input()
obj.sort()