def cat(f):
    for i in f:
        for j in open(i):
            print j
        print '--------------------------------------------------------'
cat(['test.py','test2.py'])
