def Outer(arg):
    def Inner(v1,v2):
        if v1 == v2 == 0:
            return 'Not possible'
        if v2==0:
            v1,v2=v2,v1
        if v1<0:
            v1*=(-1)
        if v2 <0:
            v2*=(-1)
        return arg(v1,v2)
    return Inner
@Outer
def Fun1(num1,num2):
    return num1/num2
print(Fun1(3,0))
print(Fun1(0,2))
print(Fun1(0,0))
print(Fun1(-3,0))
print(Fun1(5,10))