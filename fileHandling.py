f = open('MyData','r')
f1 = open('Random','w')

for data in f:
    f1.write(data)