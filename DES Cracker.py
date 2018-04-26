from pyDES import encrypt,decrypt

with open('ciphertext','r') as c:
	s=c.read()
temp=[s[i:i+2]] for i in range(0,len(s),2)]
temp=temp[:len(temp)-1]
cipher=[]
for i in range(len(temp)):
	cipher.append(int(temp[i],16))

def dec():
	key=[0xE0,0xE0,0xE0,0xE0,0xF1,0xF1,0xF1,0xF1]
	plain=decrypt(key,cipher)
	return plain

print dec()