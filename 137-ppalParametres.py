#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)>1:
	print "la cadena",sys.argv[1],"té %d caràcters"%(len(sys.argv[1]))
else :
	print "Falten paràmetres !!!"
