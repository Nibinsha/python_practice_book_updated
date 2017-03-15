def even(x):
    return x%2 == 0

def filter(f,a):
    return [i for i in a if f(i)]

print filter(even,range(10))
    
