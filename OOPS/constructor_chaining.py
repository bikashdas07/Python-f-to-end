class A:
    def __init__(self):
        self.var=10
        print(f'parent {self.var}')
        # C.__init__(self) - Infinity chaining.
class B(A):
    def __init__(self):
        self.var=20
        print(f'child-parent {self.var}')
        super().__init__()
        
class C(B):
    def __init__(self):
        self.var=30
        print(f'child {self.var}')
        #Chaining using class_reference.
        B.__init__(self)
        A.__init__(self)
        #Chaining using super()
        super().__init__()
ob1=C()