class Sample:
    v="Public Variable" #Public variable
    def __init__(self):
        self.__var = "private variable"  # Private variable
        self._var1= "protected variable"  #Protected variable

    def __M1(self):  # Private method
        return "A private method."

    def M2(self): #Public method
        return f'Apublic method that calls {self.__M1()}'
    def _M3(self):  # Protected method
        return "A protected method."
    
ob1 = Sample()
print(ob1.v)
print(Sample.v)
print(ob1.M2()) #Accessing Public Method

print(ob1._var1)
print(Sample._var1)
print(ob1._M3()) #Accessing Protected Method(Accessible only inside the package)

#ob1.__var #Private variable cannot be accessed outside the class
#ob1.__M1() #Private method cannot be accessed outside the class
#print(ob1._Sample__var)  # Accessing private variable outside the class using name
#print(ob1._Sample__M1()) #Accessing private method outside the class using name mangling

