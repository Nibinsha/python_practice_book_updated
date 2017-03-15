def treemap(f,l):
    l1 = []
    for i in l:
        if isinstance(i,list):
           l1.append(treemap(f,i))
        else:
           l1.append(f(i))
    return l1

print treemap(lambda x:x*x,[1, 4, [9, 16, [25]]])
