# _*_ coding: utf-8 _*_

def u1(f,n):
	"""Voici la valeur d'une suite au rang n définie explicitement par la fonction f
  
	:param function f: la fonction par laquelle est définie explicitement la suite
	:param int n: le rang 
	:returns: la valeur de la suite au rang n
	:rtype: float
	"""
	U= f(n)
	return U
	
def u2(f,init,n):
	"""Voici la valeur d'une suite au rang n définie par récurrence par la fonction f
  
	:param function f: la fonction par laquelle est définie la récurrence de la suite
	:param float init: la valeur du premier terme de la suite 
	:param int n: le rang 
	:returns: la valeur de la suite au rang n
	:rtype: float
	"""
	U=init
	for i in range(1,n+1):
		U += f(U)
	return U
