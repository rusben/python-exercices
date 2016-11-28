#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

num=int(raw_input("Introduce un numero:"))

noprimo=0

con=2

while (con<num):
	res=num%con
	if (res == 0): noprimo=1
	con=con+1

if (noprimo==1):
	print "el numero no es primer"
else:
	print "el numero es primer"
