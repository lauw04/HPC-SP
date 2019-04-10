# _*_ coding: utf-8 _*_

import i_rect as r
import i_trap as t
import i_boole as b
import i_simpson as s

def fn(x):
	"""Voici la fonction qui définit une fonction mathématique et la calcule en un point donné en argument

	:param float x: le point auquel on calcule la fonction 
	:returns: la valeur de la fonction au point x
	:rtype: float
	"""
	return 4.0/(1+(x-3)*(x-3))

def main():
	"""Exécute les fonctions
	"""
	print(r.rectangles(fn,0.,5.,100))
	print(t.trapezes(fn,0.,5.,100))
	print(b.boole(fn,0.,5.,100))
	print(s.simpson(fn,0.,5.,100))

main()
