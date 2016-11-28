#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Hospital.py
	Construcció d'un programa de control d'ingressos 
	a un hospital amb les operacions bàsiques */"""

from record import record 
from os import system

# Tipus data
class data(record ):
	dia = 0
	mes = 0
	any = 0

# Tipus pacient
class pacient(record ):
    codi = 0
    nom = ""
    sexe = ''
    tel = ""
    edat = 0
    pes = 0.0
    inici = data(dia=0,mes=0,any=0)

# Llista d'ingressos
ingressos =[]

opcio='z'  
comptador=0;

# Repetir
while opcio!='f' and opcio!='F' :
	#Menú
	system("clear")
	opcio=raw_input("\t\tINGRESSOS\n\ta) Alta Ingrés\n\tb) Llistar Ingressos\n\tc) Llistar Ingressos d'un pacient\n\td) Buscar Ingrés (codi)\n\te) Baixa Ingrés\n\tf) Sortir\n\tTria Una opció: ")

	#Analisi opcions

	if opcio=='a' or opcio=='A': # Inserció ordenada per pacient
		comptador+=1
		codi=comptador
		nom=raw_input("\n\tIntrodueix el nom (10 caràcters): ")
		sexe=raw_input("\tIntrodueix el sexe M/F: ")
		tel=raw_input("\tIntrodueix el telèfon (9 xifres): ")
		edat=int(raw_input("\tIntrodueix l'edat: "))
		pes=float(raw_input("\tIntrodueix el pes: "))
		dia=int(raw_input("\tIntrodueix el dia d'inici dd: "))
		mes=int(raw_input("\tIntrodueix el mes mm: "))
		any=int(raw_input("\tIntrodueix l'any aaaa: "))

		i=0
		while i<len(ingressos)-1 and ingressos[i].nom<=nom:
			i+=1
		ingressos.insert(i,pacient(codi=codi,nom=nom,sexe=sexe,tel=tel,edat=edat,pes=pes,inici=data(dia=dia,mes=mes,any=any)))
		
	elif opcio=='b' or opcio=='B': #Llista de tots els pacients
		if len(ingressos) > 0:
			print "\n\tCODI NOM        S  TELÈFON  EDAT   PES  DATA INICI"
			print "\t=================================================="
			for pac in ingressos:
				print "\t%04d %-10s %c %9s  %3d %6.2f %02d/%02d/%4d" % (pac.codi,pac.nom,pac.sexe,pac.tel,pac.edat,pac.pes,pac.inici.dia,pac.inici.mes,pac.inici.any)
		else:
			print "\n\tNo hi ha ingressos"
		raw_input()

	elif opcio=='c' or opcio=='C': #Recerca dels ingressos d'un pacient
		if len(ingressos) > 0:
			nom=raw_input("\n\tIntrodueix nom del pacient: ")
			i=0
			for pac in ingressos:
				if pac.nom==nom:
					i=i+1
					if i==1:
						print "\n\tCODI NOM        S  TELÈFON  EDAT   PES  DATA INICI"
					print "\t%04d %-10s %c %9s  %3d %6.2f %02d/%02d/%4d" % (pac.codi,pac.nom,pac.sexe,pac.tel,pac.edat,pac.pes,pac.inici.dia,pac.inici.mes,pac.inici.any)
			if i==0:
				print "\n\tPacient Inexistent"
		else :
			print("\n\tNo hi ha ingressos")
		raw_input()

	elif opcio=='d' or opcio=='D': #Recerca d'un ingrés per codi
		if len(ingressos) > 0:
			codi=int(raw_input("\n\tIntrodueix el codi de l'ingrés: "))
			i=0
			while i!=len(ingressos)-1 and ingressos[i].codi!=codi:
				i+=1
			if ingressos[i].codi==codi:
				print "\n\tCODI NOM        S  TELÈFON  EDAT   PES  DATA INICI"
				print "\t%04d %-10s %c %9s  %3d %6.2f %02d/%02d/%4d" % (ingressos[i].codi,ingressos[i].nom,ingressos[i].sexe,ingressos[i].tel,ingressos[i].edat,ingressos[i].pes,ingressos[i].inici.dia,ingressos[i].inici.mes,ingressos[i].inici.any)
			else :
				print("\n\tCodi Inexistent")
		else :
			print("\n\tNo hi ha ingressos")
		raw_input()
	
	elif opcio=='e' or opcio=='E': #Esborra un ingrés
		if len(ingressos) > 0:
			codi=int(raw_input("\n\tIntrodueix el codi de l'ingrés: "))
			i=0
			while i!=len(ingressos)-1 and ingressos[i].codi!=codi:
				i+=1
			if ingressos[i].codi==codi:
				print "\n\tCODI NOM        S  TELÈFON  EDAT   PES  DATA INICI"
				print "\t%04d %-10s %c %9s  %3d %6.2f %02d/%02d/%4d" % (ingressos[i].codi,ingressos[i].nom,ingressos[i].sexe,ingressos[i].tel,ingressos[i].edat,ingressos[i].pes,ingressos[i].inici.dia,ingressos[i].inici.mes,ingressos[i].inici.any)
				confirma=raw_input("\n\tVol esborrar el contacte? [s/n]: ")
				if confirma=='s' or confirma=='S':
					del(ingressos[i])
			else :
				raw_input("\n\tCodi Inexistent")
		else :
			raw_input("\n\tNo hi ha ingressos")

	elif opcio=='f' or opcio=='F': #Sortida
		raw_input("\n\tAdéu")
		system("clear")

