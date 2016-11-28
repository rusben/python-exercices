#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Mòdul Auxiliar 
		Obté els components d'un vector i en fa la mitjana """

MAX_VEC = 5

def obtenirVector() :
	v=[]

	for i in range (0,MAX_VEC) :
		valor=int(raw_input("Introdueix enters pos %d: "%(i+1)))
		v.append(valor)
	return v

def mitjana(v) :

	suma= 0

	for i in range (0,MAX_VEC) :
		suma=suma+v[i]

	return float(suma)/MAX_VEC

