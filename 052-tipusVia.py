#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme tipusVia.py és 
		Donat un tipus de via i un nom de via, escriu tipus amb el nom """

from os import system

# Esborrem pantalla
system("clear")
# Demanem Tipus de via i no de la via
tipus=raw_input("Introdueix el tipus de via: " )
via=raw_input("Introdueix el nom de la via: " )

if tipus=='A' :
	print "Avinguda",via
elif tipus=='C' :
	print "Carrer",via
elif tipus=='P' :
	print "Plaça",via
elif tipus=='p' :
	print "Passeig",via
elif tipus=='R' :
	print "Rambla",via
elif tipus=='V' :
	print "Via",via
else :
	print "Tipus de via incorrecte"
raw_input()
system("clear")
print "Gràcies per usar el nostre programa"

