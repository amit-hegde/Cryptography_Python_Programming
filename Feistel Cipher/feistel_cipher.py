def func(x,k):
    return bin(int(x,2)|int(k,2))
def xor(r,l):
    return bin(int(r,2)^int(l,2))
    
def encrypt(le,re,k):
#     print(p1,p2,k)
    r1=func(re,k)[2::]
    r2=xor(r1,le)[2::]
    r2="0"*(len(r1)-len(r2))+r2
#     print(r2+re)
    return r2+re

def decrypt(le,re,k):
    r1=func(re,k)[2::]
    r2=xor(r1,le)[2::]
    r2="0"*(len(r1)-len(r2))+r2
    return r2+re

p=input("Enter Plain text (in binary format): ")
t=int(input("Ënter total rounds <=16:"))
print("Enter %d KEYS"%t)
k=[]
for i in range(t):
    k.append(input("Enter Key-"+str(i+1)+" (in binary format): "))
n=len(p)
C=p
for i in range(t):
    C=encrypt(C[0:n//2],C[n//2:n],k[i])
print("Encrypted data= %s"%C)

P=C
for i in range(t):
    P=decrypt(P[0:n//2],P[n//2:n],k[i])
print("Decrypted data= %s"%P)
