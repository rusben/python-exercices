#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	CalculSuperfícies.py
		Programa que calcula les àrees d'alguns polígons
		Utilitza mòdul auxiliar d'àrees i accepta paràmetres d'entrada """

from Arees import *
from os import system
import sys

def menu():
	system("clear")
	print "\033[0;0;32m\n\t** ÀREES **"
	print "\t***********"
	print "\t\033[4;40;32mC\033[0;0;32mercle"
	print "\t\033[4;40;32mQ\033[0;0;32muadrat"
	print "\t\033[4;40;32mT\033[0;0;32mriangle"
	print "\t\033[4;40;32mR\033[0;0;32mombe"
	print "\t\033[4;40;32mS\033[0;0;32mortir"
	op=raw_input("\n\tTria una opció: \033[0m")
	return op


if len(sys.argv)>1:
	system("clear")
	opcio=sys.argv[1]
else:
	opcio=menu()

while (opcio!='s' and opcio!='S'):
	if opcio=='c' or opcio=='C': 
		try:
			r=float(raw_input("\n\tIntrodueix el radi del cercle: "))
			area=areaCercle(r)
			print "\n\t L'àrea és %.2f"%area
		except ValueError:
			print "\n\tNo heu introduït un nombre real!!!"
	elif opcio=='q' or opcio=='Q': 
		try:
			c=float(raw_input("\n\tIntrodueix el costat del quadrat: "))
			area=areaQuadrat(c)
			print "\n\t L'àrea és %.2f"%area
		except ValueError:
			print "\n\tNo heu introduït un nombre real!!!"
	elif opcio=='t' or opcio=='T': 
		try:
			b=float(raw_input("\n\tIntrodueix la base del Triangle: "))
			h=float(raw_input("\n\tIntrodueix l'altura del Triangle: "))
			area=areaTriangle(b,h)
			print "\n\t L'àrea és %.2f"%area
		except ValueError:
			print "\n\tNo heu introduït un nombre real!!!"
	elif opcio=='r' or opcio=='R': 
		try:
			D=float(raw_input("\n\tIntrodueix la diagonal major: "))
			d=float(raw_input("\n\tIntrodueix la diagonal menor: "))
			area=D*d/2
			print "\n\t L'àrea és %.2f"%area
		except ValueError:
			print "\n\tNo heu introduït un nombre real!!!"
	else:
		print '\n\tOpció incorrecta'
	raw_input()
	opcio=menu()

print '\n\tAdéu'
raw_input()
system("clear")
