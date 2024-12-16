import string
import re

autorise = string.ascii_letters + string.digits + ": +-"

liste = []

with open("test.xml", "r") as f:
	for l in f:
		result = re.search('>(.*)</', l)
		if result != None:
			liste.append(l.split('>')[0]+'>'+re.sub(r'[^.'+autorise+']', "*", result.group(1))+'</'+l.split('</')[-1])
		else:
			liste.append(l)

with open("new.xml", "w") as f2:
	for i in liste:
		f2.write(i)
