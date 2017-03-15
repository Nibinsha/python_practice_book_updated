import sys

def line(f):
    x = open(f).readlines()
    if sys.argv[1] == 'head':
       for i in x[0:2]:
           print i
    elif sys.argv[1] =='tail':
        for i in x[-3:-1]:
            print i
    else:
         print 'error'

line('txt.txt')
