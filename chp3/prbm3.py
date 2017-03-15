import os

def lis(f):
    f = os.listdir(f)
    for i in f:
        print str(i)+'  '+str(len(i))+'  '+str(os.stat(os.path.abspath(os.path.join(f,i)))[7])

lis('/home/nibinsha/Desktop/prctcebook/chp2/')
