class Sample:
    a=10
    b=50
    @classmethod
    def cm1(cls, value=100):
        cls.a=value
ob1=Sample()
ob2=Sample()
print(ob1.a)
print(ob1.b)
#Accessing classmethod using obj_ref.
ob1.cm1()
print(ob1.a)
print(ob2.b)
#Accessing classmethod using class_ref
Sample.cm1(200)
print(ob1.a)
print(ob2.b)
