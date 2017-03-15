def tree_reverse(l):
    x = l[::-1]
    l1 = []
    for i in x:
        if isinstance(i,list):
           l1.append(tree_reverse(i))
        else:
           l1.append(i)
    return l1
print tree_reverse([6, [[5, 4], 3], [2, 1]])
