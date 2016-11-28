#!/usr/bin/python
# -*- coding: utf-8 -*-

#	17.Equació2nGrau.py 
#	programa que calcula les solucions reals o imaginàries d'una equació de 2n grau amb els coeficients introduïts per l'usuari.

from math import sqrt
try: 
	try :

		print "Programa per a resoldre equacions de 2n grau"
		a = float (raw_input("Introdueix el coeficient d'x2 (a): ")) 
		b = float (raw_input("Introdueix el coeficient d'x (b): ")) 
		c = float (raw_input("Introdueix el terme independent (c): ")) 

		# Mirem si l'equació és de 2n grau
		try :
			# Calculem el discriminant per veure si és negatiu
			disc = (b*b)-(4*a*c)
			try :
				x1= (-b + sqrt(disc))/(2*a);
				x2= (-b - sqrt(disc))/(2*a);
			 	print "x1 = ", x1, " i x2 = ",x2
			except ValueError:
				print "x1 =",-b/(2*a),"+",sqrt(-disc)/(2*a)," i"
				print "x2 =",-b/(2*a),"-",sqrt(-disc)/(2*a)," i"
		except ZeroDivisionError:
			print "L'equació no és de segon grau"
	except ValueError:
		print "Els coeficients a, b i c han de ser reals"
except KeyboardInterrupt:
	print "\nSortida del programa inesperada"
