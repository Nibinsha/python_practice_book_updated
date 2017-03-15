flt = {}
def fltdict(d):
    dic = {}
    for i,v in d.items():
        if isinstance(v,dict):
           for a,b in v.items():
               dic[i+'.'+a]=b
           fltdict(dic)
        else:
           flt[i]=v
    return flt

print fltdict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
