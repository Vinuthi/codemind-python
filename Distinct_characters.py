n=input()
n=n.lower()
k=set(n)
k=list(k)
k.sort()
if(k.count(" ")>=1):
    j=k.index(" ")
    k.pop(j)
k.sort()
k="".join(k)
print(k)
