def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(n, lines):
    return (line for line in lines if len(line)>n)

def printlines(lines):
    for line in lines:
        print line

def main(n, filenames):
    lines = readfiles(filenames)
    lines = grep(n, lines)
    printlines(lines)


main(40,'test2.py'.split())
