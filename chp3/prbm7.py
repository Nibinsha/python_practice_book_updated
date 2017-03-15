import re

def make_slug(x):
    y = re.findall('\w+',x)
    z = '-'.join(y)
    print z

make_slug('--hello-   world-')    
