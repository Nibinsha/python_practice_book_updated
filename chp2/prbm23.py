import sys

def center(f):
    x = open(f).readlines()
    li = []
    for i in x:
        li.append(len(i))
    
    for j in x:
        if len(j)<max(li):
           print ' '*(max(li)-len(i)/2)+j
        else:
           print j

center('txt.txt')
