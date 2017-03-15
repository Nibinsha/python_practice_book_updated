import sys
import tablib
data = tablib.Dataset()
with open(sys.argv[1],'r') as f:
	data = f.read()
with open(sys.argv[2],'wb') as f:
	f.write(data)
