s='lala'
s.join("kurwa")

imie='kalinowska'
cecha='kurwa'




l=[]
for i in range(10,-1,-1):
    temp=l.append(i)

l.pop(5)


def fib(n):
    if n<=1:
        return n
    elif n not in cache:
        cache[n]=fib(n-1)+fib(n-2)
    return cache[n]

xs=[()]
res=[False]*2
if xs:
    res[0]=True
if xs[0]:
    res[1]=True

a=True
b=True

not (a==b)

u=bin(13)

def countBits(n):
    bit=bin(n)[2:]
    return len(bit)


def modulus(n):
    if type(n) is int:
        return n % 2
    else:
        return -1


if type([3,5,6,1]) is list:
    return

class Node:
    def __init__(self, value):    # Take children out of constructor
        self.value = value
        self.children = []     # Initialise children in the function

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, list_of_children):
        for child in list_of_children:
            self.add_child(child)

    def __repr__(self):
        return self.value # I am not a machine



def letterGraph():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    k=Node('K')
    i=Node('I')
    j=Node('J')

    a.add_children([b, c,d])
    b.add_children([e,f])
    f.add_children([i,j])
    d.add_children([g,h])
    g.add_children([k])

    print(a.value)
    print(a.children)
    print(b.children)
    print(f.children)
    print(d.children)
    print(g.children)

