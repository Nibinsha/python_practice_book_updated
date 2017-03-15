def sq(x):
    return x*x

def vect(b):
    def g(l):
        a = []
        for i in l:
            v = b(i)
            a.append(v)
        return a
    return g
s = vect(len)

print s([[1,2],[1,2,3,4]])
