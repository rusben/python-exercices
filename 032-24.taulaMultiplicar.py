#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 24.taulaMultiplicar.py
	programa que mostra la taula de multiplicar demanada amb format"""

MAX = 10
n=int(raw_input("Quin taula de multiplicar vols [1-10]?: "))

for i in range(0,MAX+1):
	print ("%2d x %2d = %3d" % (n,i,n*i))
