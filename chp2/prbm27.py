def triplets(x):
    return [(i,j,k) for i in range(x) for j in range(x) for k in range(x) if (i+j) == k and i<k and i!=0 and j<k and i<=j]

print triplets(5)
