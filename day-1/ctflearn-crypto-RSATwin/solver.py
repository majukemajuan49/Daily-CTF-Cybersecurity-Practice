from Crypto.Util.number import long_to_bytes
from sympy import totient

def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return x

def fermat(n):
	t0=isqrt(n)+1
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)
	while((temp*temp)!=((t*t)-n)):
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	return p,q

n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
e = 65537
c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

p, q = fermat(n)

assert p*q == n

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)

# OR

phi = int(totient(n))
d = pow(e, -1, phi)
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)

# flag{i_l0v3_tw1N_pr1m3s}