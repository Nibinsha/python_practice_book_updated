import sys
import textwrap

def wordwrap(f):
    s = 30
    x = open(f).readlines()
    for i in x:
        print(textwrap.fill(i,s))
wordwrap('txt.txt') 
