# _*_ coding: utf-8 _*_

def multiplication(mat,x):
	"""Voici la fonction qui calcule le produit d'une matrice par un scalaire
  
	:param list(list) mat: la matrice à multiplier
	:param float x: le scalaire par lequel on multiplie la matrice 
	:returns: le produit de la matrice par le scalaire
	:rtype: list(list)
	"""
	mul = [[] for i in range(len(mat))]
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			mul[i].append(mat[i][j]*x)
	return mul
