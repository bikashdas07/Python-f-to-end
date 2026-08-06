'''INT, FLOAT, BOOLEAN, COMPLEX, NONE'''
print('--INT--')
print(int())
n=5
print(type(n))

print('--FLOAT--')
print(float())
n1=-5.4
print(type(n1))
n1=1.2351239372300029382938493249084080324093209408324893848309032080329409408324803840830
print(n1,'Conserves 16 values after decimal(.)')
n1=841230848932849839849082394184981489.83 
print(n1,'->Values in total befor decimal(.)except 1st one')

print('--BOOL--')
print(bool())
n2=True
print(type(n2))
print('True+True is',True+True)
print('True-True is',True-True)
print('True+False is',True+False)
print('False+False is',False*True)
print('False/True is',False/True)
print('True/False not possible')

print('--COMPLEX--')
print(complex())
n3=5+7j
print(n3)
print('Real part is',n3.real)
n3=6+8J
print(n3)
print('Imaginary part is',n3.imag)
n3=10j
print(n3)
print(type(n3))

print('--None--')
print("None()-> Error, non type don't has a default object")
n4=None
print(type(n4))