import zipfile
import sys

z = zipfile.ZipFile(sys.argv[1])
for i in z.namelist():
    print 
    print "file :", i
    print
    print z.read(i)
