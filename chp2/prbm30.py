def parse_csv(f):
    x = open(f).readlines()
    print [[i.split(',')] for i in x]
        

parse_csv('parse_csv.txt')
    
