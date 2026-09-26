#We need inheritance to perform method overriding
class A:
    def M1(self):
        print('Parent class method 1')
    def M2(self):
        print('Parent class method 2')

class B(A):
    def M2(self):
        print('Child class method 2')
    def M3(self):
        print('Child class method 3')

ob=B()
ob.M1()
ob.M2()
ob.M3()