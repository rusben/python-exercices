#!/usr/bin/python
# -*- coding: utf-8 -*-

""" ExerciciRecord.py
	 exemple d'ús de record """

from record import record

class Persona(record ):
	nom = ''
	dni = ''
	edat = 0

joan = Persona(nom='Joan Pau', dni='12345678Z', edat =19)
anna = Persona(nom='Anna Mir', dni='23456789Z', edat =18)

print joan.nom
print anna.dni
print joan
print anna

persones=[]
persones.append(joan)
persones.append(anna)


print persones

print persones[2].nom
