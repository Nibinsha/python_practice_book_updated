import os
import urllib
import re
url = 'https://github.com/manimkv/Anand-Python/blob/master/anand_chp3/pgm6-antihtml.py'
basename = 'index.html'

x = urllib.urlretrieve(url,os.getcwd()+'/'+basename)
y = open(basename)
z = re.findall(r'>[^<]+<', y.read())

for i in z:
    print i[1:-1]
