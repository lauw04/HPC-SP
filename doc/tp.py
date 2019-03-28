#−∗−coding :  utf−8−∗−
def rectangles(f,a,b,n):
	S=0
	for i in xrange (0 ,n):
		xi=a+(b−a)∗i/float(n)
		xj=a+(b−a)∗(i+1)/float(n)
		S+= f((xi+xj)/2.0)∗(xj−xi)
	return S
	
def trapezes(f,a,b,n):
	S=0
	for i in xrange (0 ,n):
		xi=a+(b−a)∗i/float(n)
		xj=a+(b−a)∗(i+1)/float(n)
		S+= ((f(xi)+f(xj))/2.0)∗(xj−xi)
	return S
	
def fn(x):
	return 4.0/(1+(x−3)∗(x−3))
	
def main():
	print "par rectangles : ", rectangles(fn,0.,5.,100);
	print "par trapèzes : ", trapezes(fn,0.,5.,100);
