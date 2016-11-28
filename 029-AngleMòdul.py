#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme modulAngle.py és 
		Calcula el mòdul i l'angle d'un vector des del 0"""

from math import sqrt,atan,degrees

# Llegim dades 
x = float(raw_input("Escriu l'abcisa (0 acaba): "))
y = float(raw_input("Escriu l'ordenada (0 acaba): ")) 
#Repetir llegint abans del while
while (x!=0 or y!=0) :
	if (x != 0 ):
		modul= sqrt(x*x+y*y)
		angle= degrees(atan(y/x))
	else :
		modul=abs(y)
		if (y>0):
			angle = 90
		else :
			angle = -90

	print "El mòdul és %.2f"%modul," i l'angle és %.2f"%angle,"º"

	x = float(raw_input("Escriu l'abcisa (0 acaba): "))
	y = float(raw_input("Escriu l'ordenada (0 acaba): ")) 
	# Llegir abans de sortir

print "Gràcies per usar el nostre programa"
