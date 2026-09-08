def Dissarium(num):
    if num==0:
        return 0
    return (num%10)**len(str(num)) + Dissarium(num//10)
n=int(input('Enter the number: '))
num=n
if n>0:
    print(f'{n} is {'Dissarium' if Dissarium(num)==n else 'Not Dissarium'}')
else:
    print("Can't check")
