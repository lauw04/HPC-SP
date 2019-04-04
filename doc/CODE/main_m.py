# _*_ coding: utf-8 _*_

import addition
import multiplication
import produit
import somme

def main():
	"""Exécute les fonctions
	"""
	mat1 = [[3,5,8],[2,4,8],[9,3,1]]
	mat2 = [[2,2,4],[1,5,7],[3,8,6]]
	
	print(addition.addition(mat1,mat2))
	print(multiplication.multiplication(mat1, 2))
	print(produit.produit(mat1, mat2))
	print(somme.somme(mat1))

main()
