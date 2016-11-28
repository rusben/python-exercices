#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme qualificacioSaxona.py és 
		Donat un nom i una qualificació saxona, escriu el nom i la qualificació d'aquí"""

from os import system

# Esborrem pantalla
system("clear")
# Demanem Nom i qualificació saxona
nom=raw_input("Escriu el nom de l'alumne: " )
q=raw_input("Escriu la qualificació saxona [A-E/N]: " )

if q=='A' :
	print nom,"Excellent"
elif q=='B' :
	print nom,"Notable"
elif q=='C' :
	print nom,"Aprovat"
elif q=='D' :
	print nom,"Insuficient"
elif q=='E' :
	print nom,"Molt Deficient"
elif q=='N' :
	print nom,"No presentat"
else :
	print "Qualificació incorrecta"
raw_input()
system("clear")
print "Gràcies per usar el nostre programa"

