from math import sqrt
def calcT(d1,d2,h1,h2,v,r,s,n):
    if(d1>0):
        e1 = h2*d2
        e2= s*n
        e3= h1*d1
        q= sqrt((2*d1*s)/(v*r))
        e4=0.5*q*v*r
        e5= s*d1/q
        e6= v*(d1+d2)
        t = e1+e2+e3+e4+e5+e6
    else:
        e1 = h2*d2
        e2= s*n
        e6= v*(d1+d2)
        t = e1+e2+e6
    return t
v=int(input("masukan nilai v: "))
s=int(input("masukan nilai s: "))
h1=int(input("masukan nilai h1: "))
h2=int(input("masukan nilai h2: "))
r=float(input("masukan nilai r: "))
tmin = 99999999999999999
indexTmin=0
i=0
d1=[]
d2=[]
n=[]
l=[]
m = int(input("masukan pengulangan: "))
print("----------------------------------------------")
 
for i in range(m):
    inputL=int(input("masukan nilai L ke-"+str(i+1)+": "))
    l.append(inputL)
    inputD1=int(input("masukan nilai D1 ke-"+str(i+1)+": "))
    d1.append(inputD1)
    inputD2=int(input("masukan nilai D2 ke-"+str(i+1)+": "))
    d2.append(inputD2)
    inputN=int(input("masukan nilai n ke-"+str(i+1)+": "))
    n.append(inputN)
    print("----------------------------------------------")
    t = calcT(d1[i],d2[i],h1,h2,v,r,s,n[i])
    if(t < tmin):
        tmin =t
        indexTmin = i
    i = i +1
 
print("Nilai L = ",l[indexTmin])
print("Nilai Tmin = ",tmin)
 
