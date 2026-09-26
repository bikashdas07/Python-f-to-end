#Method overloading is also called as compile time polymorphism.
#method overloading is not possible in python but we can achieve it by using default and *args arguments.
class A:
    def M1(self,a=0,b=0):
        print(a+b)
    def M1(self,a=0,b=0,c=1):
        print(a+b+c)    
    def M2(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)
ob=A()
ob.M1(10,20) #This will call the second method and print 30
ob.M2(10,20,30)
ob.M2(10,20,30,40,50)
ob.M2()
