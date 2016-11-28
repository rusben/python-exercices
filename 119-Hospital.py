#!/usr/bin/python
# -*- coding: utf-8 -*-

from record import record 
 
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


def escriureTitol():
	print "\n\tN NOM        S Ed.  Pes     Data"
	print "\t==================================="

def escriureIngres(p):
	print "\t%d"%p.codi, "%-10s"%p.nom, "%c"%p.sexe, "%2d"%p.edat, "%6.2f"%p.pes,"%02d-%02d-%4d"%(p.inici.dia,p.inici.mes,p.inici.any)


ingressos =[]

opcio='z'  
comptador=0;
while opcio!='f' and opcio!='F' :
	opcio=raw_input("\t\tINGRESSOS\n\ta) Alta Ingrés\n\tb) Llistar Ingressos\n\tc) Llistar Ingressos d'un pacient\n\td) Buscar Ingrés (codi)\n\te) Baixa Ingrés\n\tf) Sortir\n\tTria Una opció: ")

	if opcio=='a' :
		comptador=+1
		codi=comptador
		nom=raw_input("\n\tIntrodueix el nom (10 caràcters): ")
		sexe=raw_input("\tIntrodueix el sexe M/F: ")
		tel=raw_input("\tIntrodueix el telèfon (9 xifres): ")
		edat=int(raw_input("\tIntrodueix l'edat: "))
		pes=float(raw_input("\tIntrodueix el pes: "))
		dia=int(raw_input("\tIntrodueix el dia d'inici dd: "))
		mes=int(raw_input("\tIntrodueix el mes mm: "))
		any=int(raw_input("\tIntrodueix l'any aaaa: "))
		ingressos.append(pacient(codi=codi,nom=nom,sexe=sexe,tel=tel,edat=edat,pes=pes,inici=data(dia=dia,mes=mes,any=any)))
		
	elif opcio=='b':
		if len(ingressos) > 0:
			for pac in ingressos:
				escriureIngres(pac)
		else:
			print "No hi ha ingressos"
		raw_input()

	elif opcio=='c': print "Opció c"
	elif opcio=='d': print "Opció d"
	elif opcio=='e': print "Opció e"
	elif opcio=='f':
		raw_input("\tAdéu")

