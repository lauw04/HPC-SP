# _*_ coding: utf-8 _*_

def somme(mat):
	"""Voici la fonction qui calcule la somme des éléments d'une matrice
  
	:param list(list) mat: la matrice dont il faut sommer les éléments
	:returns: la somme des éléments
	:rtype: float
	"""
	som = 0
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			som += mat[i][j]
	return som
