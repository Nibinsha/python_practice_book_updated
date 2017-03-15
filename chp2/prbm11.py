def dups(x):
    l = []
    s = []
    for i in x:
        if i not in l:
           l.append(i)
        else:
           s.append(i)
    return s

print dups([1,2,3,4,4,5,6,6,7,7])
