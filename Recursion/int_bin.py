def Binary(num,pos):
    if num==0:
        return 0
    return (num%2)*pos + Binary(num//2,pos*10)
n=int(input('Enter the number: '))
num=n
pos=1
ans=Binary(num,pos)
if n>0:
    print(f'Binary is: 0b{ans}')
else:
    print(f'Binary is: -0b{ans}')