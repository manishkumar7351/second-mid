n=input('enter a number')
l=len(n)
h=int(n)
s=0
t=n
while n>0:
    h=n%10
    s+=h**l
    n=n//10
if t==s:
    print(t,end='')
else:
    pass
