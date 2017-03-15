def enumerate(x):
    l = range(len(x))
    
    d = dict([(l[i],x[j]) for i in range(len(l)) for j in range(len(x)) if i==j]) 
    for a,b in d.items():
        print a,b
enumerate(['a','b','c'])
