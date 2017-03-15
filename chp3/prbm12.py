import sys
from inspect import getmembers,isfunction
x = __import__(sys.argv[1])
print "DESCRIPTION"
print x.__doc__
print "FUNCTION"
fun = [i for i in getmembers(x) if isfunction(i[1])]
for a in fun:
    print a[0]
