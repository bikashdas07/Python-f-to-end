'''STRING, LIST, TUPLE, SET, DICTIONARY, ARRAY'''
print('--STRING--')
print(str())
n="Hello World"
print(type(n))

print('--LIST--')
print(list())
n=[12, 34, "curie", 'a', False]
print(n)
print(type(n))

print('--TUPLE--')
n=(1,)
print(n,'Empty string')
print(type(n))
n1=(12, 'ABC', True, 45.5)
print(n1)
print(type(n1))

print('--SET-- No Duplicates')
print(set())
s={1,2,True,'M'}
print(s)
print(type(s))

print('--DICTIONARY-- No Duplicate Keys')
d={1: 'Hello', 2: 'World', 'a': True, 1: 'Money', True: 'LAXMI'}
print(d)
print(type(d))
