s='lala'
s.join("kurwa")

imie='kalinowska'
cecha='kurwa'

imie.append(imie)


l=[]
for i in range(10,-1,-1):
    temp=l.append(i)

l.pop(5)

cache: dict[int,int]={}
def fib(n):
    if n<=1:
        return n
    elif n not in cache:
        cache[n]=fib(n-1)+fib(n-2)
    return cache[n]

