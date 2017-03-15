def lensort(x):
    x.sort(key=lambda a : len(a))
    return x


print lensort(['abcde','a','abc','abcd'])
