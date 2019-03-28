#−∗−coding :  utf−8−∗−

def rectangles(f,a,b,n):
  """
  This function calculates integrals by the rectangles method
  
  Parameters
  ----------
  f : function
  a : float
    beginning of the interval
  b : float
    ending of the interval
  n : int
    number of steps

  Returns
  -------
  float
    Integral
  """
	S=0
	for i in xrange (0 ,n):
		xi=a+(b−a)∗i/float(n)
		xj=a+(b−a)∗(i+1)/float(n)
		S+= f((xi+xj)/2.0)∗(xj−xi)
	return S
	
def trapezes(f,a,b,n):
  """
  This function calculates integrals by the trapezes method
  
  Parameters
  ----------
  f : function
  a : float
    beginning of the interval
  b : float
    ending of the interval
  n : int
    number of steps

  Returns
  -------
  float
    Integral
  """
	S=0
	for i in xrange (0 ,n):
		xi=a+(b−a)∗i/float(n)
		xj=a+(b−a)∗(i+1)/float(n)
		S+= ((f(xi)+f(xj))/2.0)∗(xj−xi)
	return S
	
def fn(x):
    """
  This function defines a mathematical function
  
  Parameters
  ----------
  x : float
    a value

  Returns
  -------
  float
    The result of the function for x
  """
	return 4.0/(1+(x−3)∗(x−3))
	
def main():
  """
  This is a main
  Prints results of functions
  """
	print "par rectangles : ", rectangles(fn,0.,5.,100);
	print "par trapèzes : ", trapezes(fn,0.,5.,100);
