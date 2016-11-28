#!/usr/bin/python
# -*- coding: utf-8 -*-

from record import record 
from os import system
 
class data(record ):
	dia = 0
	mes = 0
	any = 0

class pacient(record ):
    codi = 0
    nom = ""
    sexe = ''
    tel = ""
    edat = 0
    pes = 0.0
    inici = data(dia=0,mes=0,any=0)


def escriureMenu():
	system("clear")
	print "\t\tINGRESSOS\n\ta) Alta Ingrés\n\tb) Llistar Ingressos"
	print "\tc) Llistar Ingressos d'un pacient\n\td) Buscar Ingrés (codi)"
	print "\te) Baixa Ingrés\n\tf) Sortir"
	op=raw_input("\n\tTria Una opció: ")
	return op

def escriureTitol():
	print "\n\tN NOM        S Ed.  Pes     Data"
	print "\t==================================="

def escriureIngres(p):
	print "\t%d"%p.codi, "%-10s"%p.nom, "%c"%p.sexe, "%2d"%p.edat, "%6.2f"%p.pes,"%02d-%02d-%4d"%(p.inici.dia,p.inici.mes,p.inici.any)

def introduirIngres(compt,ing):
		codi=compt
		nom=raw_input("\n\tIntrodueix el nom (10 caràcters): ")
		sexe=raw_input("\tIntrodueix el sexe M/F: ")
		tel=raw_input("\tIntrodueix el telèfon (9 xifres): ")
		edat=int(raw_input("\tIntrodueix l'edat: "))
		pes=float(raw_input("\tIntrodueix el pes: "))
		dia=int(raw_input("\tIntrodueix el dia d'inici dd: "))
		mes=int(raw_input("\tIntrodueix el mes mm: "))
		any=int(raw_input("\tIntrodueix l'any aaaa: "))
		ing.append(pacient(codi=codi,nom=nom,sexe=sexe,tel=tel,edat=edat,pes=pes,inici=data(dia=dia,mes=mes,any=any)))

def  llistarIngressos(ing):
	if len(ing) > 0:
		for pac in ing:
			escriureIngres(pac)
	else:
		print "\n\tNo hi ha ingressos"
	raw_input()

def llistarIngressosPacient(ing):
	nom=raw_input("\n\tIntrodueix el nom del pacient: ")
	trobat=False
	for pac in ing:
		if pac.nom == nom :
			if trobat == False:
				escriureTitol()
				trobat=True
			escriureIngres(pac)
	if trobat == False:
		print "\n\tNo hi ha ingressos d'aquest pacient"
	raw_input()

def posicioCodiIngres(ing,operacio):
		codi=int(raw_input("\n\tIntrodueix el codi de l'ingrés a %s: "%operacio))
		i=0
		while i<len(ing)-1 and ing[i].codi!=codi :
			i=i+1
		if ing[i].codi!=codi:
			i=-1
		return i

def buscarIngressCodi(ing):
	if len(ing) >0 :
		pos=posicioCodiIngres(ingressos,"cercar")
		if pos<0:
			print "\n\tNo existeix l'ingrés"
		else :
			escriureIngres(ing[pos])
	else :
		print "\n\tLlista d'ingressos buida"
	raw_input()

def esborrarIngres(ing):
	
	if len(ing) >0 :
		pos=posicioCodiIngres(ingressos,"esborrar")
		if pos<0:
			print "\n\tNo existeix l'ingrés"
			raw_input()
		else :
			escriureIngres(ing[pos])
			esb=raw_input("\n\tVol esborrar l'ingrés?[s/n]: ")
			if esb=='s' or esb=='S' :
				del(ing[pos])
	else :
		print "\n\tLlista d'ingressos buida"
		raw_input()

ingressos =[]

opcio='z'  
comptador=0;
while opcio!='f' and opcio!='F' :

	opcio=escriureMenu()

	if opcio=='a' :
		comptador=+1
		introduirIngres(comptador,ingressos)
	elif opcio=='b':
		llistarIngressos(ingressos)
	elif opcio=='c': 
		 llistarIngressosPacient(ingressos)
	elif opcio=='d':
		 buscarIngressCodi(ingressos)
	elif opcio=='e': esborrarIngres(ingressos)
	elif opcio=='f':
		raw_input("\n\t\tAdéu")
		system("clear")

