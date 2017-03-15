def cum(x):
    l = []
    c = 0
    for i in x:
        c+=i
        l.append(c)
    return l

print cum([4,7,9,10])
