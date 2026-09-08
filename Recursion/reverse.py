def Reverse(num,place):
    if num==0:
        return 0
    return place*(num%10) + Reverse(num//10,place//10)
num=int(input('Enter the number: '))
place = 10 ** (len(str(num))-1)
print(Reverse(num,place))

def Rev(num):
    if num==0:
        return 0
    res = res*10 + num%10
    return 