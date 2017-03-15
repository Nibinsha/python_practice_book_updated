def factorial(x):
    c = 1
    a = range(1,x+1) 
    for i in a:
        c*=i
    return c

print factorial(4)
