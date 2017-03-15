import sys

def grep(f):
    x = open(f).readlines()
    for i in x:
        if sys.argv[1] in i:
           print i

grep('txt.txt')
