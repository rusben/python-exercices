# -*- coding: utf-8 -*-

""" 	Arees.py
		Mòdul auxiliar amb les funcions que calculen les àrees d'alguns polígons """

from math import pi

def areaCercle(r):
	return pi*r*r

def areaRombe (D,d):
	return D*d/2

def areaQuadrat (c):
	return c*c

def areaTriangle (b,h):
	return b*h/2
