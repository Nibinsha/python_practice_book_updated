def cum_pro(x):
    l = []
    c = 1
    for i in x:
        c*=i
        l.append(c)
    return l

print cum_pro([1,2,3,4,5])
