class Search:

    def __init__(self,lst):
        print("Kindly Enter Numbers in sorted ascending order\n")
        self.lst = lst

    def get_input(self):
        size = int(input("How many number you want to Enter: "))
        for i in range (size):
            val = int(input(f"Enter {i+1} Number: "))
            self.lst.insert(i,val)
            i += 1

    def search_in(self):
        num = int(input("Enter number you want to search: "))
        l = 0
        u = len(self.lst) - 1
        while l <= u:
            mid =  (l+u) // 2 #Integer Division
            if self.lst[mid] == num:
                print(f"Number: {num} found at index {mid}")
                break
            elif self.lst[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
        else:
            print(f"Number: {num} Not-Found")

lst = []
obj = Search(lst)
obj.get_input()
obj.search_in()