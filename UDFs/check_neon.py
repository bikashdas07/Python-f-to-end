def Neon(num):
    num=num*2
    res=0
    while(num>0):
        res+=(num%10)
        num//=10
    return res==n
n=int(input('Enter the number: '))
num=n
print(f'{n} is {'Neon' if Neon(num) else 'Not a Neon'} Number.')