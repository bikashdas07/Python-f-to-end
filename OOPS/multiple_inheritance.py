class A:
    def __init__(self,v1):
        self.v1=v1
    def M1(self):
        print('parent M1 A')
class B:
    def __init__(self,v2):
        self.v2=v2
    def M1(self):
        print('parent M1 B')
class C(A,B):
    def __init__(self,v1=10,v2=20,v3=30):
        super().__init__(v1)
        B.__init__(self,v2) #super() doesn't work here because it will call the parent class A's constructor only.
        self.v3=v3
    def M2(self):
        print('child M2')
        super().M1()
        B.M1(self)
ob1=C(10,20)
ob1.M2()
ob1.M1() #MRO - Method Resolution Order. It will call the method of class A because it is the first parent class in the inheritance list.