def Armstrong(num):
    if num==0:
        return 0
    return (num%10)**l + Armstrong(num//10)
n=int(input('Enter the number: '))
num=n
l=len(str(num))
if n>0:
    print(f'{n} is {'armstrong' if Armstrong(num)==n else 'Not armstrong'}')
else:
    print("Can't check")
