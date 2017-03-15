def word(x):
    f = open(x).read().split()
    a= sorted(f)
    b = a[::-1]
    d = {}
    for i in b:
        d[i] = d.get(i,0)+1
    for m,n in d.items():
        print m,n
   

word('txt.txt')
