def Prime(num):
    for var in range(2,int(num**0.5)+1):
        if num%var==0:
            return 'Not a palyprime'
    f=Palindrome(num)
    return f
def Palindrome(num):
    res=0
    while (num>0):
        res=res*10+num%10
        num//=10
    if(res==n):
        return 'PalyPrime'
    return 'Not a palyprime'
def PalyPrime(num):
    f=Prime(num)
    return f
n=int(input('Enter the number: '))
num=n
if (num>1):
    print(PalyPrime(num))
else:
    print('Not a palyprime')
      