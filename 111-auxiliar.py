from math import sqrt

def mitjana(L):
	suma=0.0

	for num in L:
		suma=suma+num
	try:	
		mit = suma/len(L)
	except ZeroDivisionError:
		mit=0
	return mit


def desviacio(L):
	suma=0.0
	mit=mitjana(L)
	for num in L:
		suma=suma+(num-mit)*(num-mit)
	try:	
		desv=sqrt(suma)/len(L)
	except ZeroDivisionError:
		desv=0
	return desv

