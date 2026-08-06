num=int(input('Enter the number: '))
temp=num
while(num>9):
    res=0
    while(num!=0):
        rem=num%10
        res=res+rem*rem
        num//=10
    num=res
if(num == 1 or num == 7):
    print(f'{temp} is Happy Number')
else:
    print(f'{temp} is not a Happy Number')
