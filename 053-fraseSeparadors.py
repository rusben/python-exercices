#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme fraseSeparadors.py és 
		Llegeix una frase introduïda per l'usuari i diu quants caràcters té i quants separadors ('.',',',' ') conté """

from os import system

separadors =['.',' ',',']
 
# Esborrem pantalla
system("clear")
# Demanem la frase
frase=raw_input("Introdueix una frase: ")

compta=0
for i in range (0,len(frase)) :
	if frase[i] in separadors :
		compta=compta+1
# Mostrem resultats
print "La frasé té",len(frase), "caràcters i",compta,"separadors"
