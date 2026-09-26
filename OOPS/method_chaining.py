#Using class_reference
class A():
    v1=10
    v2=20
    def M1(self):
        print('Parent class method')

class B():  #Inheritance is optional
    v3=30
    v2=200
    def M1(self):
        print('Child class method')
        A.M1()  #Method Chaining       
ob1=B()
ob1.M1()

#Using super()
class C:
    v1=10
    v2=20
    def M2(self):
        print('Parent class method')

class D(C):  #Inheritance is mendatory
    v3=30
    v2=200
    def M2(self):
        print('Child class method')
        super().M2()  #Method chaining
ob2=D()
ob2.M2()