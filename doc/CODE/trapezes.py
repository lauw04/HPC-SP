#−∗−coding :  utf−8−∗−
	
def trapezes(f,a,b,n):
	"""Voici la fonction qui calcule l'intégrale d'une fonction donnée en paramètre par la méthode des trapèzes
  
	:param function f: la fonction dont on calcule l'intégrale par la méthode des rectangles
	:param float a: le début de l'intervalle
	:param float b: la fin de l'intervalle
	:param int n: le nombre de pas (i.e. d'intervalles) 
	:returns: la valeur de l'intégrale
	:rtype: float
	"""

	S=0
	for i in xrange (0 ,n):
		xi=a+(b-a)*i/float(n)
		xj=a+(b-a)*(i+1)/float(n)
		S+= ((f(xi)+f(xj))/2.0)*(xj-xi)
	return S
	
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
	print(trapezes(fn,0.,5.,100))
