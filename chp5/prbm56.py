import os
def cntline(f):
    for i in f:
        if '.py' in i:
           yield i

def con(pyf):
    for i in pyf:
        c =0
        for j in open(i).readlines():
            if j[0]!='#' and j!='\n':
               c+=1
        print i,c

def main(d):
    files = os.listdir(d)
    pyfi = cntline(files)
    con(pyfi)

main('/home/nibinsha/Desktop/prctcebook/chp5')
