import os
import urllib
import sys
url='http://www.facebook.com/'
if url[-1]=='/':
   basename='index.html'
else:
   basename=url.split('/')[-1]
print 'Saving  ',url,'  as ',basename
urllib.urlretrieve(url,os.getcwd()+'/'+basename)

