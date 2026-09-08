#1,2,145,40585
def Remainder(num: int) -> int:
    res=0
    while(num>0):
        r=Factorial(num%10)
        res+=r
        num//=10
    return res
def Factorial(rem : int)-> int:
    itr,fact=1,1
    while(itr<=rem):
        fact*=itr
        itr+=1
    return fact

def Strong(num : int) -> bool:
    return Remainder(num) == n

n=int(input('Enter a number: '))
num=n
print(f'{n} is {'a strong' if Strong(num) else 'not a strong'} number')
