def parse(x,y,z):
    f = open(x).readlines()
    print [[i.split(y)] for i in f if f[0] != z]


print parse('parse_csv.txt','!','#')
