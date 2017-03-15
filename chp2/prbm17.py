def reverse(f):
    y = open(f).readlines()
    for line in reversed(y):
        print line
reverse('txt.txt')
