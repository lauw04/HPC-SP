#−∗−coding :  utf−8−∗−

import rect
import trapezes
import boole
import simpson

def fn(x):
	"""Voici la fonction qui définit une fonction mathématique et la calcule en un point donné en argument

	:param float x: le point auquel on calcule la fonction 
	:returns: la valeur de la fonction au point x
	:rtype: float
	"""
	return 4.0/(1+(x-3)*(x-3))

def main():
	"""Exécute la fonction
	"""
	print(rect.rectangles(fn,0.,5.,100))
	print(trapezes.trapezes(fn,0.,5.,100))
	print(boole.boole(fn,0.,5.,100))
	print(simpson.simpson(fn,0.,5.,100))

main()
