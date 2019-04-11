# _*_ coding: utf-8 _*_

def produit(mat1,mat2):
	"""Voici la fonction qui calcule le produit de deux matrices
  
	:param list(list) mat1: première matrice à multiplier (premier facteur de l'addition)
	:param list(list) mat2: deuxième matrice à multiplier (deuxième facteur de l'addition)
	:returns: le produit des deux matrices
	:rtype: list(list)
	"""
	n1 = len(mat1)
	p1 = len(mat1[0])
	n2 = len(mat2)
	p2 = len(mat2[0])
	
	if (p1 != n2):
		return "On ne peut pas faire le produit de ces deux matrices"
	
	prod = [[0 for i in range(p2)] for j in range(n1)]
	
	for i in range(n1):
		for j in range(n2):
			for k in range(p1):
				prod[i][j] += mat1[i][k]*mat2[k][j]
	return prod
