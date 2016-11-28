#!/usr/bin/python
# -*- coding: utf-8 -*-

""" calculsVector.py
	Programa principal obtenir uns resultats d'poeracions sobre un vector.
	Author: Adrià T """

from math import sqrt


l=[];
opcio='1'
while opcio != 'e' :
	opcio=raw_input("\tCàlculs Vectorials\n\ta) Introduir vector\n\tb) Llistar vector\n\tc) Mòdul Vector\n\td) Mitjana Vector\n\te) Sortir\n\tTria una opció: ")
	# Opció introduir enters
	if opcio=='a' :
		l=[]
		continua=raw_input("Vols introduir més nombres [s/n]: ")
		while continua!='n' and continua!='N':
			n=float(raw_input("Introdueix nombre real: "))
			l.append(n)
			continua=raw_input("Vols introduir més nombres [s/n]: ")

	if opcio=='b' :
		print "\n\t(",
		for n in l:
			print n,
		print ")\n"

	if opcio=='c' :
		suma=0.0
		for n in l:
			suma=suma+n**2
		modul=sqrt(suma)
		print "\n\tel mòdul és", modul, "\n"

	if opcio=='d' :
		suma=0.0
		for n in l:
			suma=suma+n
		mitjana=suma/len(l)
		print "\n\tla mitjana és", mitjana, "\n"
