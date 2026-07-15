a=10
print(id(a))
__a=15
_1=12
_d=__a+_1
print(_d)


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

i=5 
j=5
print(id(i))
print(id(j))
print('Same memory location for different variables having same value')

a=5
b=10
c=a+b
d=c-a
a=b
c=c-5
print(a,b,c,d)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
