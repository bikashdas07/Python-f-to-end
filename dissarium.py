#Without using Built-in Functions.
num=int(input("Enter the number: "))
n=num
res=0
while(num!=0):
    rem=(num%10)
    res=(res*10)+rem
    num//=10
res2=0
count=0
ans=0
while(res!=0):
    count+=1
    res2=res%10
    d=res2**count
    ans=ans+d
    res//=10
if(ans==n):
    print(f'{n} is a Disarium number(Increasing power).')
else:
    print(f'{n} is not a Disarium number.')


#Using Built-in Functions.
a=int(input("Enter the number: "))
s=str(a)
l=len(s)
i,r,c=0,0,1
while(a!=0 and c<=l):
    r=r+int(s[i])**c
    i+=1
    c+=1
if(a==r):
    print(f'{a} is a Disarium number(Increasing Power).')
else:
    print(f'{a} is not a Disarium number.')


#Effective Solution
digit=int(input("Enter the number: "))
temp=digit
new_digit=0
s=str(digit)
length=len(s)
while(digit!=0):
    remainder=digit%10
    new_digit=new_digit+(remainder**length)
    length-=1
    digit//=10
if(new_digit==temp):
        print(f'{temp} is a Disarium number(Increasing Power).')
else:
    print(f'{temp} is not a Disarium number.')
