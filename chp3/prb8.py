import urllib
import os
import re
url = "https://python160.wordpress.com/"

a = 'link.html'


x = urllib.urlretrieve(url,os.getcwd()+'/'+a)
y = open(a)
z = re.findall(r'http://[^<]+.com', y.read())

for i in z:
    print i

