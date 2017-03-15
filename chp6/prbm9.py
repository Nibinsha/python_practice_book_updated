def permute(x):
    return [[a,b,c] for a in x for b in x for c in x if a!=b and b!=c and a!=c]

print permute([1,2,3])
