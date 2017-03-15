def zip(x,y):
    return [(x[i],y[j]) for i in range(len(x)) for j in range(len(y)) if i==j ]

print zip([1,2,3],['a','b','c'])
