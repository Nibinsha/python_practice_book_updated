import os
def cntline(f):
    a = os.listdir(f)
    for i in a:
        if '.py' in i:
           print i,len(open(i).readlines()) 

cntline('/home/nibinsha/Desktop/prctcebook/chp5')
