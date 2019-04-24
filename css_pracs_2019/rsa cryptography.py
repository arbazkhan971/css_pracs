class Rsa:
	def generator(n1,n2):
		n = n1*n2
		phi = (n1-1)*(n2-1)
		
		for i in range(2,phi):
			if gcd(i,phi)==1:
				e = i
				break
		k=0
		while(k<1000):
			if (k*phi + 1)%e==0:
				d = int((k*phi + 1)/e)
			k+=1
		
		return ((e,n),(d,n))
	def encode(text,key):
		e,n = key
		return (text**e)%n
	def decode(text):
		d,n = key
		return (text**d)%n

pub , pri = Rsa.generator(17,11)
enc = encode("arbaz",pub)
dec = decode(enc,pri)

print("encoded code",enc)
print("decoded code",dec)