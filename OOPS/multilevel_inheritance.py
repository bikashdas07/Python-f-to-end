class A:
    v1=10
    def M1(self):
        print('parent M1')
    def M2(self):
        print('Parent M2')
    
class B(A):
    v1=20
    def M1(self):
        print('child-parent M1')
    def M3(self):
        print('child-parent M3')
class C(B):
    v=30
    def M1(self):
        print('Child M1')
ob1=C()
print(ob1.v1)
ob1.M1()
ob1.M2()
ob1.M3()