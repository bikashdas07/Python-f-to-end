class A:
    v1=10
    v2=20
    def M1(self):
        print('Parent class method')
    def M2(self):
        print('Parent class method')

class B(A):
    v3=30
    v2=200
    def M3(self):
        print('Child class method')
    def M1(self):
        print('Child class method.')
    
ob1=B()
ob1.M1()
ob1.M2()
ob1.M3()
print(ob1.v2)
print(A.v2)
print(ob1.v1,B.v3)

