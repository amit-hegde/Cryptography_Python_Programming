
import numpy as np

        

def enc(x,y):
    xx=x
    yy=y

    i=np.argwhere(a2 == x)
    j=np.argwhere(a2 == y)
#     print(i,j)
    if(i[0][1]==j[0][1]):
        i1=(i[0][0]+1)%5
        j1=(j[0][0]+1)%5
        x=a2[i1][i[0][1]]
        y=a2[j1][j[0][1]]
    
    elif(i[0][0]==j[0][0]):
        i1=(i[0][1]+1)%5
        j1=(j[0][1]+1)%5
        x=a2[i[0][0]][i1]
        y=a2[j[0][0]][j1]
      
    else:
        x1=i[0][1]
        y1=j[0][1]
        x=a2[i[0][0]][y1]
        y=a2[j[0][0]][x1]
    print(xx+yy,"->",x+y)  
    return x+y   


def dec(x,y):
    xx=x
    yy=y

    i=np.argwhere(a2 == x)
    j=np.argwhere(a2 == y)
    if(i[0][1]==j[0][1]):
        i1=(i[0][0]-1)%5
        j1=(j[0][0]-1)%5
        x=a2[i1][i[0][1]]
        y=a2[j1][j[0][1]]

    elif(i[0][0]==j[0][0]):
        i1=(i[0][1]-1)%5
        j1=(j[0][1]-1)%5
        x=a2[i[0][0]][i1]
        y=a2[j[0][0]][j1]
      
    else:
        x1=i[0][1]
        y1=j[0][1]
        x=a2[i[0][0]][y1]
        y=a2[j[0][0]][x1]
    print(xx+yy,"->",x+y)  
    return x+y       


k=input("Enter Key: ")
p=input("Enter Text :")
k=k.upper()
p=p.upper()
a=[0]*25
pos=0
for i in k:
    v=i
    if(v=="I" or v=="J"):
        v='I'
    if(v not in a):
        a[pos]=v
        pos+=1

for i in range(65,(65+26)):
    v=chr(i)
    if(v=="I" or v=="J"):
        v='I'
    if(v not in a):
        a[pos]=v
        pos+=1
    
arr = np.array(a)
a2=arr.reshape(5, 5)
# print(a)
print(a2)

i=0
p1=[]
while(i<len(p)):
    if(p[i] !=" "):
        if(i==len(p)-1):  
            p1.append(p[i]+"Z")
            i+=1
        elif(p[i]==p[i+1]):
            p1.append(p[i]+"X")
            i+=1
        
        else:
            p1.append(p[i]+p[i+1])
            i+=2
# print(p1)
print("\nEncrypting.. ") 
ec=[]
for i in p1:
    ec.append(enc(i[0],i[1]))
print()    
print("Encrypted data =","".join(ec))    
print("\nDecrypting.. ")
dc=[]
for i in ec:
    dc.append(dec(i[0],i[1]))
print()
print("Decrypted data =","".join(dc))
