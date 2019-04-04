#−∗−coding :  utf−8−∗−


def boole(f,a,b,n):
	"""Voici la fonction qui calcule l'intégrale d'une fonction donnée en paramètre par la méthode des trapèzes
  
	:param function f: la fonction dont on calcule l'intégrale par la méthode des rectangles
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
		S+= (7*f(xi) + 32*f((xj+xi)/2.0) + 12*f(xj) + 32*f((3*xj-xi)/2.0) + 7*f(2*xj-xi))*(xj-xi)/90
	return S
