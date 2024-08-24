class Sorting:
    def __init__(self, lst):
        self.lst = lst

    def get_input(self):
        size = int(input("How many elements you would like to insert: "))
        for i in range(size):
            val = int(input(f"Insert {i+1} value: "))
            self.lst.insert(i,val)

    def sort(self):
        for i in range(len(self.lst)):
            minpos = i
            for j in range(i,len(self.lst)):
                if self.lst[j] < self.lst[minpos]:
                    minpos = j
            temp = self.lst[i]
            self.lst[i], self.lst[minpos] = self.lst[minpos], self.lst[i]
        print("SORTED ELEMENTS ARE: ",self.lst)

lst = []
obj = Sorting(lst)
obj.get_input()
obj.sort()