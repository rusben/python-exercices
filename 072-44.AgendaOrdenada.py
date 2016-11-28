#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 44.Agenda.py
	programa per gestionar una agenda telefònica en Python
	Utilitzem un mòdul que no és estàndard !!!! 
	record.py ha de trobar-se al mateix directori on esteu treballant """

from record import record 
from os import system
 
class contacte(record ): 
	nom = ''
	tel = '' 

agenda =[]

opcio='z'
while opcio!='e' :
	system("clear")
	opcio=raw_input("a) Introduir Contacte\nb) Llistar Contactes\nc) Buscar contacte\nd) Esborrar Contacte\ne) Sortir\n\tTria Una opció: ")
	if opcio=='a' :
		nom=raw_input("Introdueix el nom: ")
		tel=raw_input("Introdueix el telèfon: ")
		i=0
		if len(agenda) > 0:
			while i!=len(agenda) and agenda[i].nom<=nom:
				i+=1
		agenda.insert (i,contacte(nom=nom, tel=tel))
		
	elif opcio=='b':
		if len(agenda) > 0:
			print "Nom           Telèfon"
			for cont in agenda:
				print "%-10s %10s" % (cont.nom,cont.tel)
		else:
			print "Agenda Buida"
		raw_input()

	elif opcio=='c':
		if len(agenda) > 0:
			nom=raw_input("Introdueix nom del contacte: ")
			i=0
			while i!=len(agenda)-1 and agenda[i].nom!=nom:
				i+=1
			if agenda[i].nom==nom:
				print "Nom           Telèfon"
				print "%-10s %10s" % (agenda[i].nom,agenda[i].tel)
			else:
				print "Contacte Inexistent"
			raw_input()
		else :
			raw_input("Agenda Buida")

	elif opcio=='d':
		if len(agenda) > 0:
			nom=raw_input("Introdueix nom del contacte: ")
			i=0
			while i!=len(agenda)-1 and agenda[i].nom!=nom:
				i+=1
			if agenda[i].nom==nom:
				print "Nom           Telèfon"
				print "%-10s %10s" % (agenda[i].nom,agenda[i].tel)
				confirma=raw_input("Vol esborrar el contacte? [s/n]: ")
				if confirma=='s' or confirma=='S':
					del(agenda[i])
			else :
				raw_input("Contacte Inexistent")
		else :
			raw_input("Agenda Buida")

			
	elif opcio=='e':
		raw_input("Adéu")
		system("clear")


