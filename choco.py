def check(a,b):
    mini=min(a,b)
    maxi=max(a,b)
    i=(mini,maxi)
    if(i in d):
        return d[i]
    if(mini==0):
        return 0
    if(mini==1):
        return a*b
    c=maxi//mini
    ns=maxi%mini
    c+=check(ns,mini)
    d[i]=c
    return c
d={}
p=int(input())
q=int(input())
r=int(input())
s=int(input())
res=0
for i in range(p,q+1):
    for j in range(r,s+1):
        res+=check(i,j)
print(res)
