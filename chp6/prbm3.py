unf = {}
def unflat(d):
    dic = {}
    dic2 = {}
    for i,v in d.items():
        x= str(i).split('.')
        for a in x[:-1]:
            if a not in dic:
               dic[a]= dic2
            d = dic[a]
        

unflat({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
        
