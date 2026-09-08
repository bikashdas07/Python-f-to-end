def Sample(a,*args,c=100,b,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
Sample(10,100,30,40,50,60,b='kw args pos',c=99,x='abc',y='def',z=[1,2,3],)

#Packing & Un-Packing
def Sample1(a,b,c):
    print(a,b,c, sep=' ')
s=10,20,30
print(s)
print(type(s))
Sample1(*s)