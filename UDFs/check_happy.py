def Happy(h : int) -> bool:
    while h>9:
        h=Digit(h)
    return h==1 or h==7
def Digit(num :int )->int:
    res=0
    while (num>0):
        res+=(num%10)**2
        num//=10
    return res
n=int(input('Enter a number: '))
num=n
print(f'{n} is {'Happy' if Happy(num) else 'Not Happy'} number')