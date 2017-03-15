def unique(x):
    l = []
    for i in x:
        if i not in l:
           l.append(i)
    return l

print unique([1,2,3,3,4,5,5,6,6])
