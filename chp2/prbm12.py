def grplist(x,y):
    return [x[i:i+y] for i in range(0,len(x),y)]
print grplist([1,2,3,4,5,6,7,8,9],3)
