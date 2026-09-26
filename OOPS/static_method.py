class Sample:
    a=10
    b=100
    @staticmethod
    def s1():
        print('Hello')
ob1 = Sample()
ob2 = Sample()
#Accessing the static method using object_ref
ob1.s1()
#Accessing the static method using class_ref
Sample.s1()