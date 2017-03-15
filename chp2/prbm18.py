def reverse(f):
    x = open(f).readlines()
    for i in x:
        print i[::-1]

reverse('txt.txt')
