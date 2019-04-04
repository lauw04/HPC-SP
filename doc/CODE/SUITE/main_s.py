# _*_ coding: utf-8 _*_

import rang
def f1(x):
	"""Voici une fonction qui définit une fonction mathématique et la calcule en un point donné en argument

	:param float x: le point auquel on calcule la fonction 
	:returns: la valeur de la fonction au point x
	:rtype: float
	"""
	return 1+((-1)**x)/x
def f2(x):
	"""Voici une fonction qui définit une fonction mathématique et la calcule en un point donné en argument

	:param float x: le point auquel on calcule la fonction 
	:returns: la valeur de la fonction au point x
	:rtype: float
	"""
	return (2*x+3)/(x+4)
	
def main():
	"""Exécute les fonctions
	"""
	print(rang.u1(f1,4))
	print(rang.u2(f2,0,6))

main()
