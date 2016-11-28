#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import pi
from os import system

""" 	Algorisme volumSuperfícieEsfera.py 
		Calcula el volum i la superfície d'esferes de radi introduït per l'usuari fins que s'hi introdueix un 0"""
 
# Esborrem pantalla
system("clear")
# Demanem el radi
radi=float(raw_input("Escriu el radi de l'esfera (0 acaba): "))

while radi !=0 :
	if radi > 0 :
		# Mostrem resultats
		print "Volum esfera = %.2f"%((4*pi*radi*radi*radi)/3),
		print " i àrea = %.2f"%(4*pi*radi*radi)
	raw_input()
	# Esborrem pantalla
	system("clear")
	# Demanem el radi
	radi=float(raw_input("Escriu el radi de l'esfera (0 acaba): "))

print "Gràcies per usar el nostre programa"

