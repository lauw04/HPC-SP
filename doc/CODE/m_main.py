# _*_ coding: utf-8 _*_

import m_addition as a
import m_multiplication as m
import m_produit as p
import m_somme as s

def main():
	"""Exécute les fonctions
	"""
	mat1 = [[3,5,8],[2,4,8],[9,3,1]]
	mat2 = [[2,2,4],[1,5,7],[3,8,6]]
	
	print(a.addition(mat1,mat2))
	print(m.multiplication(mat1, 2))
	print(p.produit(mat1, mat2))
	print(s.somme(mat1))

main()
