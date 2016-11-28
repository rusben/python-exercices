#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme pasEsferiques.py és 
		Dóna el mòdul i l'angle d'un vector que li passem x i y"""

from math import sqrt, atan,degrees
from os import system



# Esborrem pantalla
system("clear")
# Demanem coordenades
x=float(raw_input("Escriu l'abcisa (0 acaba): " ))
y=float(raw_input("Escriu l'ordenada (0 acaba): " ))

while (x!=0 or y!=0) :
	if x!=0 :
		modul= sqrt(x*x+y*y), 
		angle=degrees (atan(y/x))
	else :
		modul=abs(y)
		if y>0:
			angle=90
		else: 
			angle=-90
	# Mostrem resultats
	print "El mòdul és: %.2f"% modul,"L'angle és: %.2f"%angle,"º" 
	# Demanem coordenades
	raw_input()
	system("clear")
	x=float(raw_input("Escriu l'abcisa (0 acaba): " ))
	y=float(raw_input("Escriu l'ordenada (0 acaba): " ))
# Sortim del bucle
print "Gràcies per usar el nostre programa"

