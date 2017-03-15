square = lambda x : x*x

def map(f,l):
    print [f(x) for x in l]

map(square,range(10))
