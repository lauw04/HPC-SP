#−∗−coding :  utf−8−∗−
	
def trapezes(f,a,b,n):
	"""Voici la fonction qui calcule l'intégrale d'une fonction donnée en paramètre par la méthode des trapèzes
  
	:param function f: la fonction dont on calcule l'intégrale par la méthode des trapèzes
	:param float a: le début de l'intervalle
	:param float b: la fin de l'intervalle
	:param int n: le nombre de pas (i.e. d'intervalles) 
	:returns: la valeur de l'intégrale
	:rtype: float
	"""

	S=0
	for i in range(0 ,n):
		xi=a+(b-a)*i/float(n)
		xj=a+(b-a)*(i+1)/float(n)
		S+= ((f(xi)+f(xj))/2.0)*(xj-xi)
	return S
