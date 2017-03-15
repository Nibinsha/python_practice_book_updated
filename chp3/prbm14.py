from bs4 import BeautifulSoup
import urllib
f = urllib.urlopen("http://www.gmail.com")
soup = BeautifulSoup(f)
print soup.findAll('a')
