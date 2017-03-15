def yrange(n):
    i = 0
    while i<n:
       yield i
       i+=1

x = yrange(5)
print x.next()
print x.next()
