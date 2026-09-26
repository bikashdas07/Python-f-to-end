class A:
    def __init__(self):
        self.var=10
    def Display1(self):
        print(f'parent {self.var}')
class B(A):
    def __init__(self):
        #A.__init__(self)   #chaining using class_reference.
        super().__init__()  #chaining using super()
        self.var=20
    def Display2(self):
        print(f'child-B {self.var}')
class C(A):
    def __init__(self):
        super().__init__()  #Chaining using super()
        self.var=30
        #A.__init__(self)   #Chaining using class_reference.
    def Display3(self):
        print(f'child-C {self.var}')    
        
ob1=B()
ob1.Display1()
ob1.Display2()

ob2=C()
ob2.Display1()
ob2.Display3()

