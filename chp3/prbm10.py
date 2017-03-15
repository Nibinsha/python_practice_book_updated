import json
import urllib
print json.load(urllib.urlopen('http://httpbin.org/get'))['origin']
