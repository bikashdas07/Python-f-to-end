b=int(input('Enter a binary Value: '))
dup=b
b=abs(b)
temp=b
count,i=0,0
while(b>0):
    rem=b%10
    i=i+rem*2**count
    count+=1
    b//10
if dup>0:
        print(f'Integer of {temp} is {i}')
else:
    print(f'Integer of {dup} is -{i}')
