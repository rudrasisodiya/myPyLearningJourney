def div(a,b):
    print(a/b)

#decorater function defination

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner

div=smart_div(div) #decorater function called
div(2,4)