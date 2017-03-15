import sys

def wrap(f):
    s = int(sys.argv[1])
    x = open(f).readlines()
    for i in x:
        print i[0:s]
        print i[s:]

wrap('txt.txt')
    
