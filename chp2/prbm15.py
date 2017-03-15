def unique(x):
    l = []
    for i in x:
        s = i.lower()
        l.append(s)
    return set(l)

print unique(['abc','Abc','ABC'])
