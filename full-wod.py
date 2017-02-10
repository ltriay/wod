#!/usr/bin/python
# -*- coding: ISO-8859-15 -*-

import sys

if len(sys.argv)!=2:
	print "Give me ONE parameter !"
	sys.exit()

trans={"a":"e","b":"q","c":"]","d":"p","e":"a","f":"j","g":"6","h":"y","i":"!", \
"j":"f","k":">|","l":"l","m":"w","n":"u","o":"o","p":"d","r":"*","s":"s","t":"+", \
"u":"n","v":"^","w":"m","x":"x","y":"h","z":"z",",":"`","`":",","!":"¡","?":"¿"}

sentence=sys.argv[1]
	
print reduce(lambda x,y:trans.get(y,y)+x,sentence,"")


	
