def product(x,n):
    if n == 0:
       return 0
    else:
       return x+ product(x,n-1)

print product(4,6)
