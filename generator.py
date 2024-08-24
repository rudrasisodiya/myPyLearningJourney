def ite():
        n = 1
        while n<=10:
            sq = n * n
            yield sq
            #yield is same like return but it returns one value at a time, we can use next() function or loop to retrive values one by one

            n +=1
values = ite()
for i in values:
    print(i)

