def extsort(x):
    x.sort(key = lambda a:len(a.split('.')[1]))
    return x


print extsort(['a.cbcde', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
