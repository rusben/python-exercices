#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)>1:
	for cadena in sys.argv :	
		print "la cadena",cadena,"té %d caràcters"%(len(cadena))
else :
	print "Falten paràmetres !!!"

# executeu-lo fent:  ./ppalParametres2.py Hola ja vinc

