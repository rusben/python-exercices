#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from auxiliar import *



def menu():
	op=raw_input("\n\ta) Introduir LLista\n\tb) Mitjana\n\tc) Moda\n\td) Desviació\n\te) Sortir\n\tTria una opció: ")
	return op
def introduirElements():
	l=[]
	try:
		demana=raw_input('Vols introduir més elements? [s/n]: ')
		while demana!='n' and demana!='N':
			num=int(raw_input('Introduir un enter: '))
			l.append(num)
			demana=raw_input('Vols introduir més elements? [s/n]: ')
	except ValueError:
		print 'No tots els valors són enters'
		l=[]
	return l

def iniciarLlista():
	l=[]
	try:
		for i in range(1,len(sys.argv)):
			num=int(sys.argv[i])
			l.append(num)
	except ValueError:
		print 'No tots els valors són enters'
		l=[]
	return l

# Programa Principal

if len(sys.argv)>1:
	lli=iniciarLlista()
else:
	lli=[]

opcio='z'
while (opcio!='e' and opcio!='E'):
	opcio=menu()
	if opcio=='a': 
		lli=introduirElements()
	elif opcio=='b': 
		m=mitjana(lli)
		print m
	elif opcio=='c': print 'En costrucció'
	elif opcio=='d': 
		d=desviacio(lli)
		print d
	elif opcio=='e': 
		print 'Adéu'
	else :
		print 'Opció incorrecta'
