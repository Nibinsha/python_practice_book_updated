import os
def count(f):
    return [i for i in f if '.py' in i]

x = os.listdir('/home/nibinsha/Desktop/prctcebook/chp3')
py = count(x)
print len(py)

