#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 44.Agenda.py
	programa per gestionar una agenda telefònica en Python
	Utilitzem un mòdul que no és estàndard !!!! 
	record.py ha de trobar-se al mateix directori on esteu treballant """

from record import record 

class contacte(record ): 
	nom = ''
	tel = '' 

agenda =[]

opcio='z'
while opcio!='e' :
	opcio=raw_input("a) Introduir Contacte\nb) Llistar Contactes\nc) Buscar contacte\nd) Esborrar Contacte\ne) Sortir\n\tTria Una opció: ")
	if opcio=='a' :
		nom=raw_input("Introdueix el nom: ")
		tel=raw_input("Introdueix el telèfon: ")
		agenda.append (contacte(nom=nom, tel=tel))

	elif opcio=='b':
		if len(agenda) > 0:
			print "Nom           Telèfon"
			for cont in agenda:
				print "%-10s %10s" % (cont.nom,cont.tel)
		else:
			print "Agenda Buida"

	#elif opcio=='c':
	#elif opcio=='d':
	elif opcio=='e':
		print "Adéu"


