class Search:

    def __init__(self,lst):
        self.lst = lst

    def get_input(self):
        size = int(input("How many number you want to Enter: "))
        for i in range (size):
            val = int(input(f"Enter {i+1} Number: "))
            self.lst.insert(i,val)
            i += 1

    def search_in(self):
        num = int(input("Enter number you want to search: "))
        size = len(self.lst)
        for i in range(size):
            if self.lst[i] == num:
                print(f"Number: {num} found at index {i}")
                break
        else:
            print(f"Number: {num} Not-Found")

lst = []

obj = Search(lst)
obj.get_input()
obj.search_in()