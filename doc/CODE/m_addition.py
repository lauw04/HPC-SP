# _*_ coding: utf-8 _*_

def addition(mat1, mat2):
	"""Voici la fonction qui calcule l'addition de deux matrices (de même taille)
  
	:param list(list) mat1: première matrice à additionner (premier terme de l'addition)
	:param list(list) mat2: deuxième matrice à additionner (deuxième terme de l'addition)
	:returns: la somme des deux matrices
	:rtype: list(list)
	"""
	n = len(mat1)
	p = len(mat1[0])
	if len(mat2) != n:
		return "On ne peut pas additionner ces deux matrices"
	elif len(mat1[0]) != p:
		return "On ne peut pas additionner ces deux matrices"
	add = [[] for i in range(n)]
	for i in range(n):
		for j in range(p):
			add[i].append(mat1[i][j] + mat2[i][j])
	return add
