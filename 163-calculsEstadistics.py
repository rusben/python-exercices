#!/usr/bin/python
# -*- coding: utf-8 -*-

""" calculsEstadistics.py
	Programa principal obtenir uns resultats estadístics.
	Author: Adrià T """

from math import sqrt


l=[];
opcio='1'
while opcio != 's' :
	opcio=raw_input("\tCàlculs Estadístics\n\ti) Introduir enters\n\tl) Llistar enters\n\tm) Mitjana\n\td) Desviació estàndard\n\ts) Sortir\n\tTria una opció: ")
	# Opció introduir enters
	if opcio=='i' :
		l=[]
		n=int(raw_input("Introdueix nombre [0 acaba]: "))
		while n!=0:
			l.append(n)
			n=int(raw_input("Introdueix nombre [0 acaba]: "))
	if opcio=='l' :
		print "\n\t(",
		for n in l:
			print n,
		print ")\n"
	if opcio=='m' :
		suma=0.0
		for n in l:
			suma=suma+n
		mitjana=suma/len(l)
		print "\n\tla mitjana és", mitjana, "\n"
	if opcio=='d' :
		suma=0.0
		for n in l:
			suma=suma+n
		mitjana=suma/len(l)

		suma=0.0
		for m in l:
			suma=suma+(n-mitjana)**2
		desviacio=sqrt(suma/len(l))
		print "\n\tla deviació és", desviacio, "\n"
