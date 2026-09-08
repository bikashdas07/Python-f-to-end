import math
def Spine(num : int) -> bool:
    l=[]
    while(num>0):
        l.append(num%10)
        num//=10
    return sum(l) == math.prod(l)
n=int(input('Enter a number: '))
num=n
print(f'{n} is {'Spine' if Spine(num) else 'not Spine'} number')