import os
def ext(f):
    d = {}
    x = os.listdir(f)
   
    for i in x:
        j = i.split('.')
        k = j[1]
        d[k] = d.setdefault(k,0)+1
    for key,val in d.items():
        print key,val

ext('/home/nibinsha/Desktop/prctcebook/chp2/')
