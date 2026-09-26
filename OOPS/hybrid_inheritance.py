#Multiple inheritances in one .py module.
class A:
    def __init__(self):
        self.var=10
        print(f'parent A {self.var}')
    def obm1(self):
        print('parent A method')
class B(A):
    def __init__(self):
        super().__init__()
        self.var=20
        print(f'child parent B {self.var}')
    def obm1(self):
        print('child parent B method')
class C(A):
    def __init__(self):
        super().__init__()
        self.var=30
        print(f'child parent C {self.var}')
    def obm1(self):
        print('child parent C method')                  
class D(B,C):
    def __init__(self):
        super().__init__()
        self.var=40
        print(f'child parent D {self.var}')
    def obm1(self):
        print('child parent D method')
class E(B,C):
    def __init__(self):
        super().__init__()
        self.var=50
        print(f'child parent E {self.var}')
    def obm1(self):
        print('child parent E method')
class F(D,E):
    def __init__(self):
        super().__init__()
        self.var=60
        print(f'child F {self.var}')
    def obm1(self):
        print('child F method') 
ob=F()
ob.obm1() #Method Resolution Order - MRO. It will call the method of class D because it is the first parent class in the inheritance list.
print(F.mro())