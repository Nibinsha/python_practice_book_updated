def anagrams(f):
    l = []
    l.append(f[0])
    
    for j in range(1,len(f)):
        flag=0
        for i in range(len(l)):
            if sorted(list(f[j]))==sorted(list(l[i][0])):
      	       l[i].append(f[j])
	       flag=1
	       break
        if flag==0:
           l.append([f[j]])
    print l
            




anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']) 
