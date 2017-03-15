def charf(f):
    x = open(f).read().split()
    d = {}
    for i in x:
        for j in i:
    #        print j.split()
            d[j] = d.get(j,0)+1
    for a,b in d.items():
        print a,b

charf('txt.txt')
