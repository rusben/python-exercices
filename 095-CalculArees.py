#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	CalculArees.py
		Programa que calcula les àrees d'alguns polígons """

from math import pi


opcio=raw_input("\n\t** ÀREES **\n\t***********\n\tc) Cercle\n\tq) Quadrat\n\tt) Triangle\n\tr) Rombe\n\ts) Sortir\n\tTria una opció: ")
while (opcio!='s' and opcio!='S'):
	if opcio=='c': 
		r=float(raw_input("\n\tIntrodueix el radi del cercle: "))
		area=pi*r*r
		print area
	elif opcio=='q': print '\n\tEn costrucció'
	elif opcio=='t': print '\n\tEn costrucció'
	elif opcio=='r': 
		D=float(raw_input("\n\tIntrodueix la diagonal major: "))
		d=float(raw_input("\n\tIntrodueix la diagonal menor: "))
		area=D*d/2
		print area
	else:
		print 'Opció incorrecta'
	raw_input()
	opcio=raw_input("\n\t** ÀREES **\n\t***********\n\tc) Cercle\n\tq) Quadrat\n\tt) Triangle\n\tr) Rombe\n\ts) Sortir\n\tTria una opció: ")
print '\n\tAdéu'
