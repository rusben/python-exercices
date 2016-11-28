#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme sumaXifres.py és 
		Suma les xifres d'un natural i calcula la mitjana per xifra """
 
nombre=int(raw_input("Escriu un nombre natural: "))
suma=0; 
xifres=0;

while (nombre>0) :
	xifres=xifres+1
	suma = suma + (nombre % 10) # Recorrem xifra a xifra
	nombre=nombre / 10; 

# Donem els resultats
if (xifres != 0) :
	print "La suma de les xifres és ",suma; 
	print "La mitjana per xifra és %.2f"%(float(suma)/xifres)
else :
	print "La suma és 0 i la mitjana per xifra és 0.00"

