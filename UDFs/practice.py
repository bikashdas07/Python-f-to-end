b=int(input('Enter a binary Value: '))
i=b
res=0
p=0
while(i>0):
    if i%10==1:
        res+=2**p
    i//=10
    p+=1
    
if b>0:
        print(f'Integer of {b} is {res}')
else:
    print(f'Integer of {b} is -{res}')
