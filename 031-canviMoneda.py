#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 	Algorisme canviMoneda.py és 
		Fa una taula del valor de las primerers 10 quantitats d'euro en la moneda donada"""
 
# Llegim la moneda i el canvi
simbol=raw_input("Introdueix el símbol de la moneda: ")
canvi= float(raw_input("Introdueix el canvi 1 € = "))

for i in range (1,11) :
	print "%2d € = %8.2f %s"%(i,i*canvi,simbol)
# Fem la taula amb el format demanat
