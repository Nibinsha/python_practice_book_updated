def invert(d):
    x = {}
    y = []
    z = []
    for i,v in d.items():
        y.append(i)
        z.append(v)
    for j in range(len(y)):
        x[z[j]] = y[j]
     

    print x

invert({'x': 1, 'y': 2, 'z': 3})
