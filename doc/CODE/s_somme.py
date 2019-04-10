import s_rang as r

def somme1(f,n):
	som=0
	for i in range(n+1):
		som += r.u1(f,n)
	return som

def somme2(f,init,n):
	som=0
	for i in range(n+1):
		som += r.u2(f,n,init)
	return som
