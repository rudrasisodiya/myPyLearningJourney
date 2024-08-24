a = 10
b = 20

# 1st way

tem = a
a = b
b = tem

print(a,b)

#2nd way

a = a + b
b = a - b
a = a - b

print(a,b)

# 3rd way

a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)

#4th way

a,b = b,a

print(a,b)