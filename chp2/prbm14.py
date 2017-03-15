def unique(x):
    l = []
    for i in x:
        s = i.lower()
        if s not in l:
           
           l.append(s)
    return l
print unique(['Abc','A','ab','abc','a'])
