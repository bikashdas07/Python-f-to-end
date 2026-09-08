def Digit(num):
    if num==0:
        return 0
    return num%10+Digit(num//10)
n=int(input('Enter a number: '))
num=abs(n)
print(Digit(num))